import datetime

import crispy_forms
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model
from templated_email import send_templated_mail

class RSVPForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = [
            'attending',
            'rsvp_message',
        ]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "id-rsvp"
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.layout = crispy_forms.layout.Layout(
            'attending',
            'rsvp_message',
            crispy_forms.layout.Submit('submit', 'Reply'),
        )
        super(RSVPForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(RSVPForm, self).save(commit=False)
        obj.rsvp_date = datetime.datetime.today()
        obj.save(*args, **kwargs)
        if obj.email:
            self.send_email(obj)
        return obj

    def send_email(self, user, *args, **kwargs):
        send_templated_mail(
            template_name='rsvp/rsvp',
            from_email='thanks@michaelblatherwick.co.uk',
            recipient_list=[user.email],
            context={'user':user,},
            bcc=['wedding@michaelblatherwick.co.uk'],
        )
