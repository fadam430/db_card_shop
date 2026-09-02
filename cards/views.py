from django.shortcuts import render
from .models import Card

# Create your views here.

def card_list(request):
    """Display all cards in a mobile-first grid"""
    cards = Card.objects.all()
    return render(request, 'templates/cards/card_list.html', {'cards': cards, 'active_page': 'cards'})
