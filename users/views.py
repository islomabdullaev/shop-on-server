from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from users.forms import ProfileModelForm
from users.models import UserModel, ProfileModel, ProfileAbstractModel


def profile(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    context = {
        "user": user,
    }
    return render(request, "profile.html", context)


def profile_update(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        country = request.POST["country"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        state = request.POST["state"]
        postcode = request.POST["postcode"]

        user_profile = ProfileModel.objects.filter(user=request.user)
        if not user_profile:
            user_profile = ProfileModel.objects.create(
                user=request.user,
                phone=phone,
                email=email,
                first_name=first_name,
                last_name=last_name,
                country=country,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                postcode=postcode,
            )
            user_profile.save()
        else:
            user_profile = ProfileModel.objects.filter(user=request.user)
            user_profile.update(
                phone=phone,
                email=email,
                first_name=first_name,
                last_name=last_name,
                country=country,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                postcode=postcode,
            )

        return redirect("users:profile")
