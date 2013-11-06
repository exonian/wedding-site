from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns("",
    url(r"^$", views.RSVPView.as_view(), name="rsvp"),
)
