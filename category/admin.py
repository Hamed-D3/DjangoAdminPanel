from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_display_links = ('title', )
    search_fields = ('title', 'parent')


admin.site.register(Category, CategoryAdmin)