from django.contrib import admin

from models import FoodOffer


class FoodOfferAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'can_bring',
        'name',
        'description',
        'portions',
        'is_vegan',
        'is_gluten_free',
        'nuts',
        'reply_date',
    )

    list_filter = (
        'can_bring',
        'is_vegan',
        'is_gluten_free',
    )

    search_fields = (
        'user',
        'name',
        'description',
        'nuts',
    )

    fields = (
        'user',
        ('get_reply_date', 'can_bring'),
        'name',
        'description',
        'portions',
        ('is_vegan', 'is_gluten_free'),
        'nuts',
    )

    readonly_fields = (
        'user',
        'get_reply_date',
    )

    def get_reply_date(self, obj):
        return obj.reply_date or ''
    get_reply_date.short_description = 'Reply date'


class FoodOfferInline(admin.StackedInline):
    model = FoodOffer


admin.site.register(FoodOffer, FoodOfferAdmin)
