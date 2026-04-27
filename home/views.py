from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

# Create your views here.

def index(request):
    """View function for home page of site."""
    
    return render(request, 'home/index.html', {'active_page': 'home'})


def favicon(request):
    """Redirect favicon requests to S3"""
    favicon_url = f"{settings.STATIC_URL}img/db_logo.png"
    return HttpResponseRedirect(favicon_url)