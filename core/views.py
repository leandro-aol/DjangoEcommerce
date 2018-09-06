from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
class IndexView(TemplateView):

    template_name = 'core/index.html'


def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido!')
    
    context = {
        'form' : form,
        'success' : success
    }
    
    return render(request, 'core/contact.html', context)


index = IndexView.as_view()
