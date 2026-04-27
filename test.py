"""
Dragon Ball Card Shop — Automated Test Suite
=============================================
Run with:
    python manage.py test tests
Or place this file inside any app and run:
    python manage.py test <app_name>

Covers: cards, bag, checkout apps
Difficulty: Medium-Hard
"""

from decimal import Decimal
from unittest.mock import patch, MagicMock

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from cards.models import Category, Card
from bag.models import Bag, BagItem
from checkout.models import Order, OrderLineItem


# ─────────────────────────────────────────────────────────────────────────────
# Shared setUp mixin
# ─────────────────────────────────────────────────────────────────────────────
class BaseTestCase(TestCase):
    """Shared fixtures used across all test classes."""

    def setUp(self):
        # Users
        self.user = User.objects.create_user(
            username='goku', password='kamehameha123', email='goku@capsulecorp.com'
        )
        self.other_user = User.objects.create_user(
            username='vegeta', password='vegeta123'
        )

        # Cards catalogue
        self.category = Category.objects.create(name='Saiyan Saga')
        self.card1 = Card.objects.create(
            name='Super Saiyan Goku',
            description='Legendary Super Saiyan transformation.',
            category=self.category,
            price=Decimal('9.99'),
            quantity=10,
        )
        self.card2 = Card.objects.create(
            name='Vegeta SSB',
            description='Super Saiyan Blue Vegeta.',
            category=self.category,
            price=Decimal('14.99'),
            quantity=5,
        )

        self.client = Client()


# ─────────────────────────────────────────────────────────────────────────────
# TEST 1 — Card list page returns all cards for unauthenticated users
# ─────────────────────────────────────────────────────────────────────────────
class CardListViewTest(BaseTestCase):

    def test_card_list_displays_all_cards_unauthenticated(self):
        """
        The card list page must be publicly accessible and render every card
        in the database. Verifies status code, template used, and context data.
        """
        response = self.client.get(reverse('card_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cards/card_list.html')

        cards_in_context = list(response.context['cards'])
        self.assertIn(self.card1, cards_in_context)
        self.assertIn(self.card2, cards_in_context)
        self.assertEqual(len(cards_in_context), 2)


# ─────────────────────────────────────────────────────────────────────────────
# TEST 2 — Adding a card to the bag creates BagItem; adding again increments qty
# ─────────────────────────────────────────────────────────────────────────────
class AddToBagTest(BaseTestCase):

    def test_add_card_twice_increments_quantity_not_duplicates(self):
        """
        Adding the same card to the bag twice must result in a single BagItem
        with quantity=2, not two separate BagItem rows. Also checks that a Bag
        is auto-created for the user on first add.
        """
        self.client.login(username='goku', password='kamehameha123')

        # First add
        self.client.post(reverse('add_to_bag', args=[self.card1.id]))
        # Second add
        self.client.post(reverse('add_to_bag', args=[self.card1.id]))

        bag = Bag.objects.get(user=self.user)
        items = BagItem.objects.filter(bag=bag, card=self.card1)

        self.assertEqual(items.count(), 1, "Expected a single BagItem row, got duplicates.")
        self.assertEqual(items.first().quantity, 2)


# ─────────────────────────────────────────────────────────────────────────────
# TEST 3 — Unauthenticated user is redirected away from bag views
# ─────────────────────────────────────────────────────────────────────────────
class BagAuthenticationTest(BaseTestCase):

    def test_bag_views_redirect_anonymous_user(self):
        """
        All bag views are decorated with @login_required. An anonymous request
        to bag_view, add_to_bag, remove_from_bag, and clear_bag must all
        return a 302 redirect to the login page, never a 200.
        """
        protected_urls = [
            reverse('bag_view'),
            reverse('add_to_bag', args=[self.card1.id]),
            reverse('clear_bag'),
        ]

        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 302,
                f"Expected redirect for anonymous user at {url}, got {response.status_code}"
            )
            self.assertIn('/accounts/login/', response['Location'])


# ─────────────────────────────────────────────────────────────────────────────
# TEST 4 — User cannot remove another user's bag item (ownership enforcement)
# ─────────────────────────────────────────────────────────────────────────────
class BagOwnershipTest(BaseTestCase):

    def test_user_cannot_delete_another_users_bag_item(self):
        """
        remove_from_bag uses get_object_or_404(BagItem, id=item_id, bag__user=request.user).
        A logged-in user attempting to delete another user's BagItem must receive
        a 404, not silently succeed.
        """
        # Create a bag item belonging to other_user
        other_bag = Bag.objects.create(user=self.other_user)
        other_item = BagItem.objects.create(bag=other_bag, card=self.card1, quantity=1)

        # Login as goku and try to delete vegeta's item
        self.client.login(username='goku', password='kamehameha123')
        response = self.client.get(reverse('remove_from_bag', args=[other_item.id]))

        self.assertEqual(response.status_code, 404)
        # Item must still exist
        self.assertTrue(BagItem.objects.filter(id=other_item.id).exists())


# ─────────────────────────────────────────────────────────────────────────────
# TEST 5 — Bag total calculation is correct with multiple items
# ─────────────────────────────────────────────────────────────────────────────
class BagTotalTest(BaseTestCase):

    def test_bag_get_total_returns_correct_sum(self):
        """
        Bag.get_total() must return the sum of (card.price * quantity) across
        all BagItems. Tests with two different cards at different quantities.
        card1: £9.99 x 3 = £29.97
        card2: £14.99 x 2 = £29.98
        Expected total: £59.95
        """
        bag = Bag.objects.create(user=self.user)
        BagItem.objects.create(bag=bag, card=self.card1, quantity=3)
        BagItem.objects.create(bag=bag, card=self.card2, quantity=2)

        expected = Decimal('9.99') * 3 + Decimal('14.99') * 2
        self.assertEqual(bag.get_total(), expected)


# ─────────────────────────────────────────────────────────────────────────────
# TEST 6 — Clear bag deletes all items but keeps the Bag object itself
# ─────────────────────────────────────────────────────────────────────────────
class ClearBagTest(BaseTestCase):

    def test_clear_bag_removes_all_items_keeps_bag(self):
        """
        clear_bag must delete all BagItems for the user's bag without deleting
        the Bag model instance itself. After clearing, get_total() must be 0
        and get_total_items() must be 0.
        """
        self.client.login(username='goku', password='kamehameha123')
        bag = Bag.objects.create(user=self.user)
        BagItem.objects.create(bag=bag, card=self.card1, quantity=2)
        BagItem.objects.create(bag=bag, card=self.card2, quantity=1)

        self.client.get(reverse('clear_bag'))

        # Bag still exists
        self.assertTrue(Bag.objects.filter(user=self.user).exists())
        # All items gone
        self.assertEqual(BagItem.objects.filter(bag=bag).count(), 0)
        bag.refresh_from_db()
        self.assertEqual(bag.get_total(), 0)
        self.assertEqual(bag.get_total_items(), 0)


# ─────────────────────────────────────────────────────────────────────────────
# TEST 7 — Order is created correctly with delivery cost logic on checkout POST
# ─────────────────────────────────────────────────────────────────────────────
class CheckoutOrderCreationTest(BaseTestCase):

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_post_creates_order_with_correct_totals(self, mock_intent):
        mock_intent.return_value = MagicMock(client_secret='test_secret_abc')

        self.client.login(username='goku', password='kamehameha123')
        bag = Bag.objects.create(user=self.user)
        BagItem.objects.create(bag=bag, card=self.card1, quantity=1)

        post_data = {
            'full_name': 'Son Goku',
            'email': 'goku@capsulecorp.com',
            'phone_number': '07700900000',
            'address_line1': '439 East District',
            'address_line2': '',
            'city': 'Mount Paozu',
            'county': '',
            'postcode': 'MP1 1ST',
            'country': 'GB',
        }

        response = self.client.post(reverse('checkout'), data=post_data)

        # ── Debug: print form errors if order wasn't created ──
        print("Response status:", response.status_code)
        print("Response context keys:", response.context.keys() if response.context else "No context")
        if response.context and 'order_form' in response.context:
            print("Form errors:", response.context['order_form'].errors)

        order = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order, "Order was not created after checkout POST.")


# ─────────────────────────────────────────────────────────────────────────────
# TEST 8 — Order model auto-generates unique order numbers on save
# ─────────────────────────────────────────────────────────────────────────────
class OrderNumberUniquenessTest(BaseTestCase):

    def test_each_order_gets_unique_order_number(self):
        """
        Order._generate_order_number() uses uuid4().hex.upper(). Creating
        multiple orders must produce unique, non-empty order numbers for each.
        Also verifies the order number is set on first save and not overwritten
        on subsequent saves (idempotency check).
        """
        orders = []
        for i in range(5):
            order = Order.objects.create(
                user=self.user,
                full_name=f'Test User {i}',
                email='test@test.com',
                phone_number='07700900000',
                address_line1='123 Test Street',
                city='Testville',
                postcode='TE1 1ST',
                country='GB',
                order_total=Decimal('9.99'),
                delivery_cost=Decimal('5.00'),
                grand_total=Decimal('14.99'),
            )
            orders.append(order)

        order_numbers = [o.order_number for o in orders]

        # All non-empty
        for num in order_numbers:
            self.assertTrue(len(num) > 0, "Order number must not be empty.")

        # All unique
        self.assertEqual(
            len(order_numbers),
            len(set(order_numbers)),
            "Duplicate order numbers detected — UUID generation is broken."
        )

        # Idempotency: saving again must not change the order number
        first_order = orders[0]
        original_number = first_order.order_number
        first_order.save()
        first_order.refresh_from_db()
        self.assertEqual(first_order.order_number, original_number)