import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from cards.models import Card
from bag.models import Bag, BagItem


# Create your models here

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=20, null=False, editable=False)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    address_line1 = models.CharField(max_length=80, blank=False, null=False)
    address_line2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=40, blank=False, null=False)
    county = models.CharField(max_length=80, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=False, null=False)
    country = models.CharField(max_length=40, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    
    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """Update grand total each time a line item is added, accounting for delivery costs"""
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    def save(self, *args, **kwargs):
        """Override the save method to set the order number if it hasn't been set already"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    card = models.ForeignKey('cards.Card', null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def save(self, *args, **kwargs):
        """Override the save method to set the lineitem total and update the order total"""
        self.lineitem_total = self.card.price * self.quantity
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Card {self.card.name} on order {self.order.order_number}'