from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category

# Create your views here.

class ProductsListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        # category = get_object_or_404(Category, slug = self.kwargs['slug'])
        # return Product.objects.filter(category=category)
        return Product.objects.filter(category__slug = self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug = self.kwargs['slug'])
        return context


class ProductListView(generic.ListView):

    template_name = 'catalog/product.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.get(slug = self.kwargs['slug'])


product_list = ProductsListView.as_view()
category = CategoryListView.as_view()
product = ProductListView.as_view()