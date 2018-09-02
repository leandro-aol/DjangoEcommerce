from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contato(request):
    return render(request, 'core/contato.html')

def produto(request):
    return render(request, 'core/produto.html')

def produtos(request):
    return render(request, 'core/produtos.html')
