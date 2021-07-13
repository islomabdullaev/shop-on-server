from django.urls import path

from pages.views import ContactTemplateView, IndexTemplateView

app_name = "pages"

urlpatterns = [
    path("contact/", ContactTemplateView.as_view(), name="contact" ),
    path("", IndexTemplateView.as_view(), name="home"),
]