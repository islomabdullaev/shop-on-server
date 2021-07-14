
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


