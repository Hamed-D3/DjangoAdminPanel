from django.contrib import admin
from .models import GeneralSetting, Category

# Register your models here.
admin.site.register(GeneralSetting)
admin.site.register(Category)