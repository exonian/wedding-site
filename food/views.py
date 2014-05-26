from braces.views import FormValidMessageMixin, LoginRequiredMixin
from django.views.generic import UpdateView

import forms
from .models import FoodOffer

class FoodView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = 'food/food.html' 
    form_class = forms.FoodForm
    form_valid_message = "Thanks for replying!"
    success_url = "/"

    def get_object(self):
        obj, created = FoodOffer.objects.get_or_create(user=self.request.user)
        return obj
