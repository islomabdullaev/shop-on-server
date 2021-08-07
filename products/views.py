from django.http import request
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, ProductTagModel, BrandModel, SizeModel, ColorModel


class ProductsListView(ListView):
    paginate_by = 3
    template_name = "shop.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["brands"] = BrandModel.objects.all()
        context["sizes"] = SizeModel.objects.all()
        context["colors"] = ColorModel.objects.all()
        return context

    def get_queryset(self):
        model = ProductModel.objects.all()

        q = self.request.GET.get("q")
        if q:
            model = model.filter(title__icontains=q)

        cat = self.request.GET.get("cat")
        if cat:
            model = model.filter(category_id=cat)
        brand = self.request.GET.get("brand")
        if brand:
            model = model.filter(brand_id=brand)

        tag = self.request.GET.get("tag")
        if tag:
            model = model.filter(tags__id=tag)

        color = self.request.GET.get("color")
        if color:
            model = model.filter(colors__id=color)

        size = self.request.GET.get("size")
        if size:
            model = model.filter(sizes__id=size)

        sort = self.request.GET.get("sort")
        if sort == "-price":
            model = model.order_by("-price")
        elif sort == "price":
            model = model.order_by("price")

        return model


class ProductDetailView(DetailView):
    template_name = "shop-details.html"
    model = ProductModel
