import crispy_forms
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model

class RSVPForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['attending']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "id-rsvp"
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.layout = crispy_forms.layout.Layout(
            'attending',
            crispy_forms.layout.Submit('submit', 'Reply'),
        )
        super(RSVPForm, self).__init__(*args, **kwargs)
