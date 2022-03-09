from django.contrib import auth, messages
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
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        confirm_password = request.POST["password2"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("accounts:signup")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect("accounts:signup")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    auth.login(request, user)
                    messages.success(request, "You are now logged in")
                    return redirect("pages:home")
                    user.save()
                    messages.success(request, "You are registered successfully.")
                    redirect("accounts:login")
        else:
            messages.error(request, "password do not match")
            return redirect("accounts:signup")
    else:
        return render(request, "accounts/registration.html")


def logout(request):
    auth.logout(request)
    return redirect("pages:home")

