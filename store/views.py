from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django import forms   

# Create your views here.
def category(request, foo):
    #Replace Hyphens with spaces
    foo = foo.replace('-', ' ')
    #Grab the category from the url
    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That Category Doesn't Exist..."))
        return redirect('home')
    
def category_summary(request):
	categories = Category.objects.all()
	return render(request, 'category_summary.html', {"categories":categories})   






def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product' : product
    }
    return render ( request, 'product.html', context) 
    

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In Successfully"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, plaese try again"))
            return redirect('login')
    else:    
        context = {
    }   
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method ==  "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate (username=username, password=password)
            login(request, user)
            messages.success(request, ("You Have Register Successfully"))
            return redirect('home')
        else:
            messages.success(request, ("There was a problem, please register agian"))
            return redirect('home')
    else:

        context = {
            'form':form
    }
        return render(request, 'register.html', context)