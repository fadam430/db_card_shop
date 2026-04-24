from django.shortcuts import render
from .models import Card, Category

# Create your views here.

def card_list(request):
    """Display all cards in a mobile-first grid"""
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})
