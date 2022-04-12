from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from home.models import WebSiteSetting as Setting

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Setting.objects.all():
            context['setting'] = Setting.objects.all()[0]
        else:
            context['setting'] = {
                'name':'setting',
                'url':'http://site.com',
                'logo':'',
                'favico':'',
            }
        return context