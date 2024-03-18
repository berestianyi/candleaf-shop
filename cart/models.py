from users.models import User
from products.models import Product
from django.db import models


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    products = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_sum(self):
        return sum(product.total_price() for product in self.products.all())



