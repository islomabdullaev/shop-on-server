from django.urls import path

from products import views
from products.views import ProductsListView, ProductDetailView, update_wishlist, update_cart, CartListView

app_name = "products"

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/wishlist/", update_wishlist, name="update-wishlist"),
    path("<int:pk>/cart/", update_cart, name="update-cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path('cart/', CartListView.as_view(), name='cart'),
    path("", ProductsListView.as_view(), name="list")
]
