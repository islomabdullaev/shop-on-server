from django.db import models
from django.utils.translation import gettext as _

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=64, verbose_name=_("full name"))
    avatar = models.ImageField(upload_to="authors-avatar", verbose_name=_("avatar"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return  self.full_name

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")


class PostTagModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_("title"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("post tag")
        verbose_name_plural = _("post tags")


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    image = models.ImageField(upload_to="posts", verbose_name=_("image"))
    banner = models.ImageField(upload_to="posts-banner", verbose_name=_("banner"))
    author = models.ForeignKey(AuthorModel, related_name="posts", on_delete=models.PROTECT, verbose_name=_("author"))

    tags = models.ManyToManyField(PostTagModel, related_name="post", verbose_name=_("tags"))

    content = models.TextField(verbose_name=_("content"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name =_("post")
        verbose_name_plural =_("posts")





