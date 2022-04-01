from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300, null=True, verbose_name="دسته‌بندی")
    parent = models.ForeignKey('self', default=True, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name='زیردسته')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title