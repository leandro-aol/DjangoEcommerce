from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm

# Create your views here.


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:index')


register = RegisterView.as_view()
