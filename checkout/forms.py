from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number', 'address_line1', 'address_line2', 'city', 'county', 'postcode', 'country']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_texts = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2 (optional)',
            'city': 'City',
            'county': 'County (optional)',
            'postcode': 'Postal Code',
            'country': 'Country',
        }
        self.fields['full_name'].widget.attrs['auto-focus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholder_texts[field]} *"
            else:
                placeholder = placeholder_texts[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False