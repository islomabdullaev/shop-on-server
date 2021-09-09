from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from users.forms import ProfileModelForm
from users.models import UserModel, ProfileModel


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "profile.html"
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse("users:profile")

    def get_object(self, queryset=None):
        if hasattr(self.request.user, "profile"):
            return self.request.user.profile
        return ProfileModel.objects.create(user=self.request.user)

