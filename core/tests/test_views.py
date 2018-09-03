from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):
    # É executado, para cada teste, no início do teste
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:index')

    # É executado, para cada teste, no final do teste
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/index.html')
