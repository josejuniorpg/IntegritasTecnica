# Django imports
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Third-party imports
from model_utils.models import TimeStampedModel


# Create your models here.

class User(AbstractUser, TimeStampedModel):
    """Default user for TwoScoPoe. The default user type is  common."""

    class Types(models.TextChoices):
        SUPERUSER = "SUPERUSER", "Superuser"
        COMMON = "COMMON", "Common"
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

    base_type = Types.COMMON

    email = models.EmailField(_("email address"), unique=True)
    type = models.CharField(
        _("User Type"), max_length=50, choices=Types.choices, default=base_type)
    profile_image = models.ImageField(upload_to='users/profileImages', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = self.Types.SUPERUSER
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class Spy(models.Model):
    """Extra fields for the Spy user type."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gadgets = models.TextField()


class SpyProxy(User):
    """Proxy model for the Spy user type. This model can access the fields of Spy model,
    using the extra_fields property."""
    base_type = User.Types.SPY
    # The import here is for  avoid circular import
    from .managers import SpyManager
    objects = SpyManager()

    class Meta:
        proxy = True

    @property
    def extra_fields(self):
        return self.spy

    def whisper(self):
        return "whisper"


class Driver(models.Model):
    """Extra fields for the Driver user type."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    year = models.IntegerField()


class DriverProxy(User):
    """Proxy model for the Driver user type. This model can access the fields of Driver model,
    using the extra_fields property."""
    base_type = User.Types.DRIVER
    # The import here is for  avoid circular import
    from .managers import DriverManager
    objects = DriverManager()

    class Meta:
        proxy = True

    @property
    def extra_fields(self):
        return self.driver

    def accelerate(self):
        return "Go faster"
