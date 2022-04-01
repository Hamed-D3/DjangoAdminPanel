from django.contrib import admin
from .models import GeneralSetting, Category

# Register your models here.
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'website_url', 'website_addr', 'website_email', 'website_phone')
    list_display_links = ('website_name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_display_links = ('title', )
    search_fields = ('title', 'parent')


admin.site.register(GeneralSetting, GeneralSettingAdmin)
admin.site.register(Category, CategoryAdmin)