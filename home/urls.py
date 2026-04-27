
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', views.favicon, name='favicon'),
]
