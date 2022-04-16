from django.views.generic import TemplateView

# models
from home.models import WebSiteSetting, ContactUsSetting, AboutUsSetting

# Create your views here.
def get_setting_sidebar():
    setting_info = {}

    setting = WebSiteSetting.objects.all()[0]
    setting_info['general'] = {'name': WebSiteSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'general'}

    setting = ContactUsSetting.objects.all()[0]
    setting_info['contactus'] = {'name': ContactUsSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'contactus'}

    setting = AboutUsSetting.objects.all()[0]
    setting_info['aboutus'] = {'name': AboutUsSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'aboutus'}

    return setting_info



class IndexView(TemplateView):
    template_name = 'profiles/index.html'

    # get name of setting, slug and it type and send it to the template    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = get_setting_sidebar()
        return context