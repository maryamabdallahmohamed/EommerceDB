from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'home.html' , context)


def about(request):
    context={}
    return render(request, 'about.html' , context)


def contact(request):
    context={}
    return render(request, 'contact.html' , context)


def products(request):
    context={}
    return render(request, 'products.html' , context)


def single_product(request):
    context={}
    return render(request, 'single_product.html' , context)


def mens(request):
    context={}
    return render(request, 'mens.html' , context)


def womens(request):
    context={}
    return render(request, 'womens.html' , context)


def kids(request):
    context={}
    return render(request, 'kids.html' , context)


def cart(request):
    context={}
    return render(request, 'cart.html' , context)