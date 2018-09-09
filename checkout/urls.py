"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    create_cartitem,
    cart_item,
    checkout,
    order_list,
    order_detail,
)

app_name = 'checkout'

urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', create_cartitem, name='create_cartitem'),
    path('carrinho/', cart_item, name='cart_item'),
    path('finalizando/', checkout, name='checkout'),
    path('meus-pedidos/', order_list, name='order_list'),
    path('meus-pedidos/<int:pk>', order_detail, name='order_detail'),
]
