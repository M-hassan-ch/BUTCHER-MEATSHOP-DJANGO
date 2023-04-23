from django.urls import path
from .views import *

urlpatterns = [
    path('', products_view, name = ""),
    path('productDetails/<int:id>', prodDetails_view, name="productDetails"),
    path('addToCart/<int:id>', addToCart_view, name="addToCart"),
    path('cart/', showCart_view, name="showCart"),
    path('remove/<int:id>', removeCartItem, name="remove")
]
