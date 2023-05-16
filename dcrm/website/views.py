from django.shortcuts import render

# authentication, login, logout imported
from django.contrib.auth import authenticate, login, logout
#message when log in log out
from django.contrib import messages


# Create your views here.
#define home request
def home(request):
    return render(request, 'home.html', {})

#define user log in and log out request
def login_user(request):
    pass
def logout_user(request):
    pass
