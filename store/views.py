from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    
    context = {
        'products' : products
    }
    
    return render ( request, 'home.html', context)

def about(request):
    
    context = {
        
    }
    return render(request, 'about.html', context)