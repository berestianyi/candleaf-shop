from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('discovery/<slug:category_slug>/', name='category'),
    path('products/<slug:detail_slug>/', views.detail, name='detail'),
    path('products/', views.discovery, name='discovery'),
    path('test/', views.test, name='test'),
]