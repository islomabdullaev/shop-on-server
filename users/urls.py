from django.urls import path

from users.views import ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("user/", ProfileUpdateView.as_view(), name="profile"),

]