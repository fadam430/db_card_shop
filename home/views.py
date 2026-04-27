from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """View function for home page of site."""
    
    return render(request, 'home/index.html', {'active_page': 'home'})


def favicon(request):
    """Handle favicon request - return 204 No Content"""
    return HttpResponse(status=204)