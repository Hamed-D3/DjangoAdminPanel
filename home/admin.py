from django.contrib import admin
from .models import GeneralSetting

# Register your models here.
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'website_url', 'website_addr', 'website_email', 'website_phone')
    list_display_links = ('website_name', )


admin.site.register(GeneralSetting, GeneralSettingAdmin)