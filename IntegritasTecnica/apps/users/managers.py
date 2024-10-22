# Django Imports
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.db import models, transaction

# Local Imports
from .models import Spy, User


class SpyManager(UserManager, models.Manager):
    """The Managers for User Type Spy. get_queryset helps for filter only spys"""

    @transaction.atomic
    def create_user(self, username, email=None, password=None, gadgets=None, **extra_fields):
        try:
            user = User(username=username, email=email, password=password, **extra_fields)
            user.full_clean()  # Validate User Fields before save.
            user = super().create_user(username=username, email=email, password=password, **extra_fields)
            spy = Spy(user=user, gadgets=gadgets)
            spy.full_clean()
            spy.save()
            return user
        except ValidationError as e:
            raise ValidationError(f"Failed to create Spy: {str(e)}")

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=get_user_model().Types.SPY)


class DriverManager(models.Manager):
    """The Managers for User Type Driver. get_queryset helps for filter only drivers"""

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=get_user_model().Types.DRIVER)
