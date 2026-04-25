from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from cards.models import Card
from .models import Bag, BagItem


@login_required
def bag_view(request):
    """Display shopping bag"""
    bag, created = Bag.objects.get_or_create(user=request.user)
    return render(request, 'bag/bag.html', {'bag': bag, 'active_page': 'bag'})


@login_required
def add_to_bag(request, card_id):
    """Add card to shopping bag"""
    card = get_object_or_404(Card, id=card_id)
    bag, created = Bag.objects.get_or_create(user=request.user)
    
    bag_item, item_created = BagItem.objects.get_or_create(bag=bag, card=card)
    if not item_created:
        bag_item.quantity += 1
    bag_item.save()
    
    return redirect('bag_view')


@login_required
def update_bag_item(request, item_id):
    """Update quantity of item in bag"""
    if request.method == 'POST':
        bag_item = get_object_or_404(BagItem, id=item_id, bag__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            bag_item.quantity = quantity
            bag_item.save()
        
        return redirect('bag_view')


@login_required
def remove_from_bag(request, item_id):
    """Remove item from shopping bag"""
    bag_item = get_object_or_404(BagItem, id=item_id, bag__user=request.user)
    bag_item.delete()
    return redirect('bag_view')


@login_required
def clear_bag(request):
    """Clear entire shopping bag"""
    bag = get_object_or_404(Bag, user=request.user)
    bag.items.all().delete()
    return redirect('bag_view')
