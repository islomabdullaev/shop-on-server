from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("pages:home")
        else:
            return redirect("accounts:login")
    return render(request, "accounts/login.html")


def signup(request):
    pass


def logout(request):
    auth.logout(request)
    return redirect("pages:home")

