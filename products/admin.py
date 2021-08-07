from django.contrib import admin
from django.utils.safestring import mark_safe

from products.forms import ColorAdminForm
from products.models import CategoryModel, ProductTagModel, ProductModel, BrandModel, ColorModel, SizeModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ["code", "color", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["code"]
    form = ColorAdminForm

    def color(self, obj):
        text = "&nbsp" * 10
        return mark_safe(f"<div style='background-color: {obj.code}'>{text}</div>")


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "discount", "created_at"]
    list_filter = ["category", "tags", "created_at"]
    search_fields = ["title"]
    autocomplete_fields = ["category", "tags", "brand", "colors", "sizes"]


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]