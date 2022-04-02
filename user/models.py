from django.db import models

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام")
    show_name = models.CharField(max_length=300, verbose_name="نام نمایشی")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سطح دسترسی"
        verbose_name_plural = "دسترسی‌ها"

    def __str__(self) -> str:
        return self.show_name


class Role(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام")
    permission = models.ManyToManyField(Permission, blank=True, verbose_name='سطح دسترسی')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "نقش"
        verbose_name_plural = "نقش‌ها"

    def __str__(self):
        return self.name

    def show_permission_name(self):
        return '، '.join([str(permission) for permission in self.permission.all()])
    show_permission_name.short_description = 'سطح دسترسی‌ها'