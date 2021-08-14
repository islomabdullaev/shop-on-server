from django.urls import path

from products.views import ProductsListView, ProductDetailView, update_wishlist, WishListView, update_cart
app_name = "products"

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/wishlist/", update_wishlist, name="update-wishlist"),
    path("<int:pk>/cart/", update_cart, name="update-cart"),
    path("wishlist/", WishListView.as_view(), name="wishlist"),
    path("", ProductsListView.as_view(), name="list")
]
