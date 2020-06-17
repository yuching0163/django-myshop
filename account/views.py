from django.shortcuts import render, get_object_or_404
from .form import RegistrationForm, LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from shop.models import Category
from cart.models import Items

def register(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect("/account/")
    else:
        form = RegistrationForm()
    return render(request, 'account/registration.html', {'form': form, 'categories': categories})

def login(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'account/login.html', {'form': form, 'message': '密碼錯誤 請重試'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'categories': categories})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/dashboard')

def dashboard(request):
    categories = Category.objects.all()
    name = str(request.user)
    purchaser = Items.objects.filter(name=name)

    return render(request, 'account/dashboard.html', {'categories': categories, 'purchaser': purchaser})
