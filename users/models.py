from django.contrib.auth.models import AbstractUser
from django.db import models

class WeddingUser(AbstractUser):
    """
    Just an extension of the Django user model
    """

    attending = models.NullBooleanField()
