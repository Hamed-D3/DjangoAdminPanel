from django.contrib import admin
from .models import GeneralSetting, WebSiteSetting, AboutUsSetting, ContactUsSetting

# Register your models here.
admin.site.register(GeneralSetting)
admin.site.register(WebSiteSetting)
admin.site.register(AboutUsSetting)
admin.site.register(ContactUsSetting)