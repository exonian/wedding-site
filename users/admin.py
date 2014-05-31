import datetime

from django.contrib import admin
from django.utils import timezone
from models import WeddingUser

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'long_name',
        'email',
        'has_logged_in',
        'last_login',
        'get_rsvp_date',
        'get_rsvp',
    )

    list_filter = (
        'attending',
        'is_staff',
    )

    search_fields = (
        'short_name',
        'long_name',
        'email',
    )

    def get_rsvp_date(self, obj):
        return obj.rsvp_date or ''
    get_rsvp_date.short_description = 'RSVP date'

    def get_rsvp(self, obj):
        return self.get_rsvp_date(obj) and obj.get_attending_display()
    get_rsvp.short_description = 'RSVP'

    def has_logged_in(self, obj):
        date = obj.last_login
        if not date:
            return False
        return date > timezone.make_aware(
            datetime.datetime(2014,1,1),
            timezone.get_default_timezone()
        )
    has_logged_in.boolean = True

admin.site.register(WeddingUser, UserAdmin)
