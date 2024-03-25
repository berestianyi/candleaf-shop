from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from users.models import User
from products.models import Product


def shopping_cart(request):
    cart = Cart.objects.first()

    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context=context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.first()
    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    cart.products.add(cart_item)
    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))


def subtract_from_cart(request, product_id):
    cart = Cart.objects.first()
    cart_item = CartItem.objects.filter(product_id=product_id, cart=cart).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))


def remove_from_cart(request, product_id):
    cart_item = CartItem.objects.get(product_id=product_id)
    cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))
