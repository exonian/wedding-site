from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Logged-in home page
    """

    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return IndexView.as_view()(request, *args, **kwargs)
        return super(HomeView, self).dispatch(request, *args, **kwargs)


class IndexView(TemplateView):
    """
    Logged-out home page
    """

    template_name = "index.html"
