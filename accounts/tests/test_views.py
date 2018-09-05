from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {
            'username' : 'testuserregister',
            'email' : 'test@test.com',
            'password1' : 'liflhj4iuo3h345',
            'password2' : 'liflhj4iuo3h345'
        }

        response = self.client.post(self.register_url, data)

        index_url = reverse(settings.LOGIN_REDIRECT_URL)

        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {
            'username' : 'testuserregister',
            'password1' : 'liflhj4iuo3h345',
            'password2' : 'liflhj4iuo3h345'
        }

        response = self.client.post(self.register_url, data)

        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')