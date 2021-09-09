from django.contrib import admin

from users.models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name"]
