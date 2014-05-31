from django.contrib import admin

from models import FoodOffer


class FoodOfferInline(admin.StackedInline):
    model = FoodOffer
