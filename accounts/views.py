from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model

from .forms import UserAdminCreationForm

User = get_user_model()

# Create your views here.



class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['username', 'name', 'email']
    success_url = reverse_lazy('accounts:index')
    
    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:index')

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
