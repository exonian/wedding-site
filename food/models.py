from django.db import models
from django.utils.translation import ugettext_lazy as _


class FoodOffer(models.Model):

    CHOICE_YES = 1
    CHOICE_MAYBE = 0
    CHOICE_NO = -1

    CHOICES = (
        (CHOICE_YES, "Yes"),
        (CHOICE_MAYBE, "Not sure"),
        (CHOICE_NO, "No"),
    )

    user = models.OneToOneField('users.WeddingUser')

    can_bring = models.IntegerField(
        _('can you bring any food?'),
        choices = CHOICES,
        default = CHOICE_MAYBE,
    )

    name = models.CharField(_('dish name'), max_length=200, blank=True)
    description = models.TextField(_('description'), blank=True)

    portions = models.CharField(
        _('number of portions'),
        max_length=200,
        blank=True,
    )

    is_vegan = models.IntegerField(
        _('vegan?'),
        choices = CHOICES,
        default = CHOICE_MAYBE,
    )

    is_gluten_free = models.IntegerField(
        _('gluten free?'),
        choices = CHOICES,
        default = CHOICE_MAYBE,
    )
    reply_date = models.DateField(
        blank = True,
        null = True,
    )

    def __unicode__(self):
        return self.name

    def get_bringing_statuses(self):
        return (
            (self.CHOICE_YES, "will"),
            (self.CHOICE_MAYBE, "might"),
            (self.CHOICE_NO, "won't"),
        )

    def get_bringing_status(self):
        return '{} be able to bring food'.format(
            dict(self.get_bringing_statuses())[self.can_bring]
        )
