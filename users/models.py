from django.contrib.auth.models import AbstractUser
from django.db import models

class WeddingUser(AbstractUser):
    """
    Just an extension of the Django user model
    """

    ATTENDING_YES = 1
    ATTENDING_MAYBE = 0
    ATTENDING_NO = -1
    ATTENDING_CHOICES = (
        (ATTENDING_YES, "Yes, I'd love to!"),
        (ATTENDING_MAYBE, "I'm not sure yet - I'll have to get back to you"),
        (ATTENDING_NO, "I'm afraid I can't make it"),
    )

    attending = models.IntegerField(
        'Are you able to attend?',
        choices = ATTENDING_CHOICES,
        default = ATTENDING_MAYBE,
    )
