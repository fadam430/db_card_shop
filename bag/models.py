from django.db import models
from django.contrib.auth.models import User
from cards.models import Card


class Bag(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bag for {self.user.username}"

    def get_total(self):
        """Calculate total price of all items in bag"""
        return sum(item.get_subtotal() for item in self.items.all())

    def get_total_items(self):
        """Get total quantity of items in bag"""
        return sum(item.quantity for item in self.items.all())


class BagItem(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name='items')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card.name} x {self.quantity}"

    def get_subtotal(self):
        """Calculate subtotal for this item"""
        return self.card.price * self.quantity
