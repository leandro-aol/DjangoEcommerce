from django.shortcuts import render

from .models import Product, Category

# Create your views here.

def products(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category' : slug,
        'products' : Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)
