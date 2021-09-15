from django.urls import path

from orders.views import CheckoutTemplateView, OrderCreateView, OrderHistoryTemplateView

app_name = "orders"

urlpatterns = [
    path("checkout/", CheckoutTemplateView.as_view(), name="checkout-view"),
    path("checkout/save/", OrderCreateView.as_view(), name="checkout-save"),
    path("order/history", OrderHistoryTemplateView.as_view(), name="order-history")
]