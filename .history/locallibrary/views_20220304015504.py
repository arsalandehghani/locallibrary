from django.shortcuts import render
from django.views import generic
from . import models

class Index(generic.TemplateView):
    template_name = 'catalog/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
