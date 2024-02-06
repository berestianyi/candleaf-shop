from django.db import models
from django.urls import reverse


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField(default=20)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(blank=True, upload_to='products/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-quantity']
        indexes = [
            models.Index(fields=['-quantity'])
        ]

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'detail_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

