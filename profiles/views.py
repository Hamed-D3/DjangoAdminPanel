from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'profiles/index.html'

    # get name of setting, slug and it type and send it to the template    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context