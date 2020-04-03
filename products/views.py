from django.shortcuts import render


# Create your views here.
from .models import Product

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    template_name='products/home.html'
    return render(request, template_name, context) 

def all(request):
    template_name='products/all.html'
    products = Product.objects.all()
    context = {'products':products}
    return render(request, template_name, context)