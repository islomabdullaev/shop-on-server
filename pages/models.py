
from django.db import models
from django.utils.translation import  gettext as _

class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    email = models.EmailField(max_length=50, verbose_name=_("email"))
    message = models.TextField(verbose_name=_("message"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")


class BannerModel(models.Model):
    collection = models.CharField(max_length=32, verbose_name=_("collection"))
    title = models.CharField(max_length=64, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    image = models.ImageField(upload_to="banners", verbose_name=_("image"))
    is_active = models.BooleanField(default=False, verbose_name=_("is active"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("banner")
        verbose_name_plural = _("banners")