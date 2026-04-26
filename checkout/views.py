from django.contrib import messages

from django.shortcuts import render, redirect, reverse
from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty. Please add items before checking out.")
        return redirect(reverse('bag_view'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    return render(request, template, context)