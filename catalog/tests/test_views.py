from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from catalog.models import Category, Product


class ProductsViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:products')
        self.client = Client()
        self.products = mommy.make(Product, _quantity=10)

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/products.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        products = response.context['products']
        self.assertEquals(products.count(), 10)
