from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import WebSiteSetting as Setting

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(pk=1)
        return context