from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import TemplateView

from .forms import ContactForm

# Create your views here.
class IndexView(TemplateView):

    template_name = 'core/index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_mail()
        success = True
    
    context = {
        'form' : form,
        'success' : success
    }
    
    return render(request, 'core/contact.html', context)
