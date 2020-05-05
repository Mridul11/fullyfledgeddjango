from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth import authenticate, login , get_user_model, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import ContactForm, LoginForm, RegisterForm
import logging 


def home_page(request):
    context = {
        'title' : 'Ecommerce HomePage',
        'content': 'Welcome to Homepage!'
    }
    return render(request, 'ecommerce/home.html', context)

# @login_required(login_url='login-route')
def about_page(request):
    context = {
        'title' : 'About Page',
        'content' : 'Welcome to the About Page!'
    }
    return render(request, 'ecommerce/about.html', context)

def contact_page(request):
    c_form = ContactForm(request.POST or None)
    context = { 
        "title": "Contact Page",
        "content" : "Please contact us here!",
        "form" : c_form
    }

    if request.method == 'POST':
        if c_form.is_valid():
            print(c_form.cleaned_data)
        # print(request.POST)
    return render(request, 'ecommerce/contact.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = { 'form' : login_form }
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Loggedin Successfully!')
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home-route')   
            else:
                context = { 'form' : login_form }
            # print(request.user.is_authenticated)
            print(login_form.cleaned_data)
    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = { "register_form" : register_form }
    if request.method == 'POST':
        if register_form.is_valid():
            print(register_form.cleaned_data)
            username = register_form.cleaned_data.get("username")
            email = register_form.cleaned_data.get("email")
            password = register_form.cleaned_data.get("password")
            user = User.objects.create_user(username, email, password)
            print(user)
            return redirect('login-route')
    return render(request, 'auth/register.html', context)

def logout_page(request):
    try:
        logout(request)
        messages.danger(request, f"Logged out successfully!")
    except Exception as e:
        logging.info(e)
    return redirect('login-route')


