from django.urls import path
from .views import AddToCartView, CartView, RemoveFromCartView

urlpatterns = [
 
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(), name='cart'),
   path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
