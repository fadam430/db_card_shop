from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from bag.models import Bag

def checkout(request):
    try:
        bag = request.user.bag
        bag_items = bag.items.all()
    except Exception:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('view_bag'))

    if not bag_items.exists():
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('view_bag'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'bag_items': bag_items,
        'bag_total': bag.get_total(),
    }
    return render(request, 'checkout/checkout.html', context)