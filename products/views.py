from django.views.generic import ListView, DetailView

from products.models import ProductModel


class ProductsListView(ListView):
    paginate_by = 3
    template_name = "shop.html"

    def get_queryset(self):
        return ProductModel.objects.all()

class ProductDetailView(DetailView):
    template_name = "shop-details.html"
    model = ProductModel
