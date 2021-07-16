from django.views.generic import  ListView

from products.models import ProductModel


class ProductsListView(ListView):
    template_name = "shop.html"

    def get_queryset(self):
        return ProductModel.objects.all()

