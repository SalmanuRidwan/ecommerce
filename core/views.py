from django.shortcuts import render
from .models import Item


def home(request):
    context = {}
    return render(request, 'home.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)

def product(request):
    context = {}
    return render(request, 'product.html', context)