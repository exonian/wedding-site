from braces.views import LoginRequiredMixin
from django.views.generic import UpdateView

class RSVPView(LoginRequiredMixin, UpdateView):
    template_name = 'rsvp/rsvp.html' 

    def get_object(self):
        return self.request.user
