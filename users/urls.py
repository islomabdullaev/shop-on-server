from django.urls import path

from users.views import profile, profile_save

app_name = "users"

urlpatterns = [
    path("user/", profile, name="profile"),
    path("profile-save/", profile_save, name="profile-save"),

]
