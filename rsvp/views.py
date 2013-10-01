from braces.views import FormValidMessageMixin, LoginRequiredMixin
from django.views.generic import UpdateView

import forms

class RSVPView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = 'rsvp/rsvp.html' 
    form_class = forms.RSVPForm
    form_valid_message = "Thanks for replying!"
    success_url = "/"

    def get_object(self):
        return self.request.user
