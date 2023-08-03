from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.http import HttpRequest


# Create your views here.

# def login_view(request: HttpRequest):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect('/')
#         return render(request, 'auth/login.html')
#     username = request.POST["username"]
#     email = request.POST["email"]
#     password = request.POST["password"]
#
#     user = authenticate(request, username=username, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/')


def login_user(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')


def logout_user(request):
    logout(request)
    return redirect('index')

