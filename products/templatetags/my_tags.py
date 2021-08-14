from django.template import Library

from products.models import WishlistModel

register = Library()


@register.simple_tag
def get_default_range(request):
    price = request.GET.get('price_filter')
    if price:
        price_from, price_to = price.split(';')
        return f'from: {price_from}, to: {price_to},'
    return ''


@register.filter
def in_wishlist(product, user):
    return WishlistModel.objects.filter(user=user, product=product).exists()


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])
