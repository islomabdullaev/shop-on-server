from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_("title"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at "))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class ProductTagModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_("title"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")


class BrandModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_("title"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")


class ColorModel(models.Model):
    code = models.CharField(max_length=32, verbose_name=_("code"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("color")
        verbose_name_plural = _("colors")


class SizeModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_("title"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("size")
        verbose_name_plural = _("sizes")


class ProductModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_("title"))
    image = models.ImageField(upload_to="products", verbose_name=_("image"))
    price = models.FloatField(verbose_name=_("price"))
    real_price = models.FloatField(default=0, verbose_name=_("real_price"))
    discount = models.PositiveSmallIntegerField(default=0)
    short_description = models.TextField(verbose_name=_("short description"))
    long_description = models.TextField(verbose_name=_("long description"))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name=_("products"),
        verbose_name=_("category")
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name=_("brand"),
        null=True
    )

    tags = models.ManyToManyField(
        ProductTagModel,
        related_name="products",
        verbose_name=_("tags")
    )

    colors = models.ManyToManyField(
        ColorModel,
        related_name="products",
        verbose_name=_("color"),
    )

    sizes = models.ManyToManyField(
        SizeModel,
        related_name="products",
        verbose_name=_("size"),
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.discount:
            return (100 - self.discount) / 100 * self.price
        return self.price

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def __str__(self):
        return self.title

    def get_related(self):
        return self.category.products.order_by("-pk").exclude(pk=self.pk)[:4]

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
