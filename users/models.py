from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class ProfileAbstractModel(models.Model):
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class ProfileModel(ProfileAbstractModel):
    user = models.OneToOneField(UserModel, related_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile: {str(self.user)}"

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"