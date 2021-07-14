from django.contrib import admin

from .models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "created_at"]
    list_filter = ["created_at"]

