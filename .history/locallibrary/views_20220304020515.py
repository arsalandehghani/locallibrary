from django.views import generic

class Index(generic.TemplateView):
    template_name = 'locallibrary/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
