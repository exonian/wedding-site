from braces.views import LoginRequiredMixin
from django.views.generic import UpdateView

import forms

class RSVPView(LoginRequiredMixin, UpdateView):
    template_name = 'rsvp/rsvp.html' 
    form_class = forms.RSVPForm

    def get_object(self):
        return self.request.user
