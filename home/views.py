from django.views.generic import TemplateView, UpdateView
from home.models import WebSiteSetting, AboutUsSetting, ContactUsSetting

from profiles.views import get_setting_sidebar

from home.forms import WebSiteSettingForm, AboutUsSettingForm, ContactUsSettingForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if WebSiteSetting.objects.all():
            context['setting'] = WebSiteSetting.objects.all()[0]
            context['settings'] = get_setting_sidebar()
        else:
            context['settings'] = get_setting_sidebar()
            context['setting'] = {
                'name':'setting',
                'url':'http://site.com',
                'logo':'',
                'favico':'',
            }
        return context


class WebSiteSettingView(UpdateView):
    model = WebSiteSetting
    form_class = WebSiteSettingForm
    template_name = 'home/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = get_setting_sidebar()
        context['verbose_name'] = WebSiteSetting._meta.verbose_name_raw
        return context


class AboutUsSettingView(UpdateView):
    model = AboutUsSetting
    form_class = AboutUsSettingForm
    template_name = 'home/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = get_setting_sidebar()
        context['verbose_name'] = AboutUsSetting._meta.verbose_name_raw
        return context



class ContactUsSettingView(UpdateView):
    model = ContactUsSetting
    form_class = ContactUsSettingForm
    template_name = 'home/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = get_setting_sidebar()
        context['verbose_name'] = ContactUsSetting._meta.verbose_name_raw
        return context