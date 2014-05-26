
from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = patterns("",

    ("^admin/", include(admin.site.urls)),

    url("^$", views.HomeView.as_view(), name="home"),
    ("^rsvp/", include("rsvp.urls")),
    ("^gifts-food/food/", include("food.urls")),
    ("^account/signup/$", 'django.views.defaults.page_not_found'),
    ("^", include("mezzanine.urls")),

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
