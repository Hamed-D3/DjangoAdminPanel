from django.core.validators import validate_image_file_extension, URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError(f"فقط میتونی یک تنظیمات برای سایتت تنظیم کنی! همونی که موجوده رو ویرایش کن.")

class GeneralSetting(models.Model):
    website_name = models.CharField(max_length=300, null=True, blank=True, default="پنل ادمین جنگو", verbose_name="نام")
    website_logo = models.ImageField(upload_to='website/', null=True, blank=True, default='default/logo.png', validators=[validate_image_file_extension], verbose_name="لوگو")
    website_favico = models.ImageField(upload_to='website/', null=True, blank=True, default='default/ico.png', validators=[validate_image_file_extension], verbose_name="فیو آیکون")
    website_url = models.URLField(default='http://site.com', null=True, blank=True, validators=[URLValidator], verbose_name="آدرس اینترنتی")
    website_email = models.EmailField(default='info@site.com', null=True, blank=True, validators=[EmailValidator], verbose_name="ایمیل")
    website_phone = models.CharField(max_length=30, default='+98 021 123456', null=True, blank=True, verbose_name="شماره تماس")
    website_addr = models.CharField(max_length=1000, null=True, blank=True, default="تهران - سید خندان - واحد 2", verbose_name='آدرس')
    terms = models.TextField(default='قوانین استفاده از وبسایت...', null=True, blank=True, verbose_name='قوانین')
    about_us = models.TextField(default='درباره ما...', null=True, blank=True, verbose_name='درباره')

    class Meta:
        verbose_name = "تظیمات وب سایت"
        verbose_name_plural = "تظیمات وب سایت"

    def __str__(self) -> str:
        return self.website_name

    def clean(self):
        validate_only_one_instance(self)


class Category(models.Model):
    title = models.CharField(max_length=300, null=True, verbose_name="دسته‌بندی")
    parent = models.ForeignKey('self', default=True, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name='زیردسته')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title