from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.shopping_cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add'),
    path('subtract/<int:product_id>/', views.subtract_from_cart, name='subtract'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove'),
]
