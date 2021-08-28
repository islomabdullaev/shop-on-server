from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Min
from django.http import request
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, ProductTagModel, BrandModel, SizeModel, ColorModel, \
    WishlistModel


class ProductsListView(ListView):
    template_name = "shop.html"
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["brands"] = BrandModel.objects.all()
        context["sizes"] = SizeModel.objects.all()
        context["colors"] = ColorModel.objects.all()
        context["max_price"],  context["min_price"] = ProductModel.objects.aggregate(
            Max("real_price"), Min("real_price")
        ).values()
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

        price_filter = self.request.GET.get("price_filter")
        if price_filter:
            price_from, price_to = price_filter.split(";")
            model = model.filter(real_price__gte=price_from, real_price__lte=price_to)

        sort = self.request.GET.get("sort")
        if sort == "-price":
            model = model.order_by("-price")
        elif sort == "price":
            model = model.order_by("price")

        return model


class ProductDetailView(DetailView):
    template_name = "shop-details.html"
    model = ProductModel


class WishListView(LoginRequiredMixin, ListView):
    template_name = "wishlist.html"

    def get_queryset(self):
        return ProductModel.objects.filter(wishlist__user=self.request.user)


class CartListView(ListView):
    template_name = 'shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.get_from_cart(cart)

@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    WishlistModel.add_or_delete(request.user, product)

    return redirect(request.GET.get('next', '/'))


@login_required
def update_cart(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    cart = request.session.get("cart", [])
    if product.pk in cart:
        cart.remove(product.pk)
    else:
        cart.append(product.pk)
    request.session["cart"] = cart
    print(request.session["cart"])

    return redirect(request.GET.get("next", "/"))
