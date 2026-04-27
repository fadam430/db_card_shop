from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.models import Bag
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    try:
        bag = request.user.bag
        bag_items = bag.items.all()
    except Exception:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('bag_view'))

    if not bag_items.exists():
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('bag_view'))

    # ── Always create intent so client_secret is always available ──
    bag_total = bag.get_total()
    stripe_total = round(bag_total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency='gbp',
    )

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.order_total = bag_total
            order.delivery_cost = settings.STANDARD_DELIVERY_COST if bag_total < settings.FREE_DELIVERY_THRESHOLD else 0
            order.grand_total = order.order_total + order.delivery_cost
            order.save()
            for item in bag_items:
                OrderLineItem.objects.create(
                    order=order,
                    card=item.card,
                    quantity=item.quantity,
                    lineitem_total=item.get_subtotal(),
                )
            bag_items.delete()
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form.")
    else:
        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'bag_items': bag_items,
        'bag_total': bag_total,
        'grand_total': bag_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  
        'client_secret': intent.client_secret,             
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order {order_number} confirmed!')
    return render(request, 'checkout/checkout_success.html', {'order': order})