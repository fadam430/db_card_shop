from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag_view'),
    path('add/<int:card_id>/', views.add_to_bag, name='add_to_bag'),
    path('update/<int:item_id>/', views.update_bag_item, name='update_bag_item'),
    path('remove/<int:item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('clear/', views.clear_bag, name='clear_bag'),
]