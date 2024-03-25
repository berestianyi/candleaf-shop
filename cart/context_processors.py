from .models import Cart


def cart(request):
    # Здесь ваша логика для получения данных о корзине
    # Например, использование сессии:
    cart_exist = Cart.objects.first()
    return {'cart':  cart_exist}
