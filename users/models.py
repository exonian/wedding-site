from django.contrib.auth.models import AbstractUser
from django.db import models

from wedding.utils import cap_first

class WeddingUser(AbstractUser):
    """
    Just an extension of the Django user model
    """

    ATTENDING_YES = 1
    ATTENDING_MAYBE = 0
    ATTENDING_NO = -1
    ATTENDING_CHOICES = (
        (ATTENDING_YES, "Yes"),
        (ATTENDING_MAYBE, "Maybe"),
        (ATTENDING_NO, "No"),
    )

    attending = models.IntegerField(
        'Are you able to attend?',
        choices = ATTENDING_CHOICES,
        default = ATTENDING_MAYBE,
    )
    rsvp_message = models.TextField(
        "Add a message, if you'd like",
        blank = True,
    )

    number = models.IntegerField(
        default = 1,
    )

    short_name = models.CharField(
        blank = True,
        max_length = 255,
    )

    long_name = models.CharField(
        blank = True,
        max_length = 255,
    )

    def get_short_name(self):
        return self.short_name or self.long_name or ''

    def get_full_name(self):
        return self.long_name or self.short_name or ''

    def is_multiple_guests(self):
        if self.number > 1:
            return True
        return False

    def get_user_pronoun_dict(self):
        """
        Returns a dictionary of pronouns and verbs referring to the user,
        which require knowledge of whether it represents a single wedding
        guest or multiple guests.
        """
        if self.is_multiple_guests():
            pronoun_dict = {
                "user": "we",
                "user_is": "we're",
                "user_will": "we'll",
                "user_would": "we'd",
            }
        else:
            pronoun_dict = {
                "user": "I",
                "user_is": "I'm",
                "user_will": "I'll",
                "user_would": "I'd",
            }
        return pronoun_dict

    def get_customised_attending_choices(self):
        return (
            (self.ATTENDING_YES,
             cap_first("Yes, {user_would} love to!".format(**self.get_user_pronoun_dict()))),
            (self.ATTENDING_MAYBE,
             cap_first("{user_is} not sure yet - {user_will} have to get back to you".format(**self.get_user_pronoun_dict()))),
            (self.ATTENDING_NO,
             cap_first("{user_is} afraid {user} can't make it".format(**self.get_user_pronoun_dict()))),
        )
