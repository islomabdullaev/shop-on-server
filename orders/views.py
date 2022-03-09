from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, ListView

from orders.forms import OrderModelForm
from orders.models import OrderModel
from products.models import ProductModel
from users.models import ProfileModel


class CheckoutTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = self.request.session.get('cart', [])

        products = ProductModel.get_from_cart(cart)

        context['profile'] = self.request.user.profile
        context['products'] = products
        context['sum'] = products.aggregate(Sum('real_price'))['real_price__sum']

        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse('pages:home')

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])

        products = ProductModel.get_from_cart(cart)

        form.instance.user = self.request.user
        form.instance.total_price = products.aggregate(Sum('real_price'))['real_price__sum']

        order = form.save()

        order.products.set(products)
        order.save()

        self.request.session['cart'] = []

        return redirect(self.get_success_url())


class OrderHistoryTemplateView(LoginRequiredMixin, ListView):
    template_name = "order_history.html"

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
