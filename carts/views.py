from django.shortcuts import render 
from django.http import request


def cart_home(request):
    key = request.session.session_key
    print(key)
    return render(request, "carts/home.html")
    
