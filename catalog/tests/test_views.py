from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from catalog.models import Category, Product

import math


class ProductListTestCase(TestCase):

    count_itens = 10
    itens_per_page = 3
    pages_number = math.ceil(count_itens / itens_per_page)

    def setUp(self):
        self.url = reverse('catalog:products')
        self.client = Client()
        self.products = mommy.make(Product, _quantity=self.count_itens)

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        products = response.context['products']
        self.assertEquals(products.count(), self.itens_per_page)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, self.pages_number)

    def test_page_not_found(self):
        response = self.client.get('{}?page={}'.format(self.url, self.pages_number + 1))
        self.assertEquals(response.status_code, 404)
