from home.models import WebSiteSetting, ContactUsSetting, AboutUsSetting


def get_setting_sidebar(request):
    setting_info = {}

    setting = WebSiteSetting.objects.all()[0]
    setting_info['general'] = {'name': WebSiteSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'general'}

    setting = ContactUsSetting.objects.all()[0]
    setting_info['contactus'] = {'name': ContactUsSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'contactus'}

    setting = AboutUsSetting.objects.all()[0]
    setting_info['aboutus'] = {'name': AboutUsSetting._meta.verbose_name_raw, 'slug': setting.slug, 'type': 'aboutus'}

    return {'settings': setting_info}