from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"
