from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product, Category


def index(request):
    products_data = Product.objects.all()
    context = {
        'mainpage_products': products_data[:8],
        'all_products': products_data,
        'popular_products': products_data[:4],
        'my_range': range(5),

    }
    return render(request, 'products/index.html', context=context)


def about(request):
    return render(request, 'products/about.html')


def detail(request, detail_slug):
    slug_detail = get_object_or_404(Product, slug=detail_slug)

    data = {
        'product': slug_detail,
    }
    return render(request, 'products/detail.html', context=data)


def discovery(request):
    products_data = Product.objects.all()
    context = {
        'all_products': products_data,
    }
    return render(request, 'products/discovery.html', context=context)


def sort_by_category(request, category_slug):
    category_info = get_object_or_404(Category, slug=category_slug)
    context = {
        'category': category_info,
    }
    return render(request, 'products/')


def test(request):
    return render(request, 'products/test.html')