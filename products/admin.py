from django.contrib import admin

from products.models import CategoryModel, ProductTagModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "discount", "created_at"]
    list_filter = ["category", "tags", "created_at"]
    search_fields = ["title"]
    autocomplete_fields = ["category", "tags"]
