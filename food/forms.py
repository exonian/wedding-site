import datetime

import crispy_forms
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from templated_email import send_templated_mail

from .models import FoodOffer

class FoodForm(forms.ModelForm):

    class Meta:
        model = FoodOffer
        fields = [
            'can_bring',
            'name',
            'description',
            'portions',
            'is_vegan',
            'is_gluten_free',
        ]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "id-food"
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.layout = crispy_forms.layout.Layout(
            crispy_forms.layout.Fieldset(
                '',
                'can_bring',
            ),
            crispy_forms.layout.Fieldset(
                '',
                'name',
                'description',
            ),
            crispy_forms.layout.Fieldset(
                '',
                'portions',
                'is_vegan',
                'is_gluten_free',
            ),
            crispy_forms.layout.Submit('submit', 'Reply'),
        )
        super(FoodForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(FoodForm, self).save(commit=False)
        obj.reply_date = datetime.datetime.today()
        obj.save(*args, **kwargs)
        self.send_emails(obj)
        return obj

    def send_emails(self, food, *args, **kwargs):
        context = {
            'user': food.user,
            'food': food,
            'site': Site.objects.get_current(),
            'url': reverse('food'),
        }
        # to the user
        if food.user.email:
            send_templated_mail(
                template_name='food/food',
                from_email='wedding@michaelblatherwick.co.uk',
                recipient_list=[food.user.email],
                context=context,
            )
        # to us
        send_templated_mail(
            template_name='food/food-notification',
            from_email='wedding@michaelblatherwick.co.uk',
            recipient_list=['wedding@michaelblatherwick.co.uk'],
            context=context,
        )
