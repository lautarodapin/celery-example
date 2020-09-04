from django.views.generic import TemplateView

from .tasks import hello_world
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hello_world.delay()
        return context
    