from django.template import Library


register = Library()


@register.simple_tag
def get_default_range(request):
    price = request.GET.get('price_filter')
    if price:
        price_from, price_to = price.split(';')
        return f'from: {price_from}, to: {price_to},'
    return ''
