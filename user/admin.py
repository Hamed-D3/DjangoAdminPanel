from django.contrib import admin
from .models import Permission, Role

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_name')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_permission_name')


admin.site.register(Permission, PermissionAdmin)
admin.site.register(Role, RoleAdmin)