from django.shortcuts import render
from django.http import Http404 , HttpRequest


# Create your views here.
from .models import Product, ProductImage

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains = q)
        context = {'query':q,'products':products}
        template_name='products/results.html'
    else:
        context = {}
        template_name='products/home.html'
    return render(request, template_name, context) 


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

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        #images = product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        context = {'product':product,'images':images}
        template_name='products/single.html'
        return render(request, template_name, context)
    except:
        raise Http404("Question does not exist")