from django.core.validators import validate_image_file_extension, URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models

# Create your models here.
def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError(f"فقط میتونی یک تنظیمات برای سایتت تنظیم کنی! همونی که موجوده رو ویرایش کن.")


class GeneralSetting(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "تظیمات کلی"
        verbose_name_plural = "تظیمات کلی"

    def __str__(self):
        return self.name


class WebSiteSetting(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True, default="پنل ادمین جنگو", verbose_name="نام")
    logo = models.ImageField(upload_to='website/', null=True, blank=True, default='default/logo.png', validators=[validate_image_file_extension], verbose_name="لوگو")
    favico = models.ImageField(upload_to='website/', null=True, blank=True, default='default/ico.png', validators=[validate_image_file_extension], verbose_name="فیو آیکون")
    url = models.URLField(default='http://site.com', null=True, blank=True, validators=[URLValidator], verbose_name="آدرس اینترنتی")
    slug = models.SlugField(default='general-setting', verbose_name="نشانک")
    parent_setting = models.OneToOneField(GeneralSetting, on_delete=models.CASCADE, verbose_name="زیرمجموعه تنظیمات")

    class Meta:
        verbose_name = "عمومی"
        verbose_name_plural = "عمومی"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('home:website-setting', args=(self.slug, ))

    def clean(self):
        validate_only_one_instance(self)


class AboutUsSetting(models.Model):
    about_us = models.TextField(default='درباره ما...', null=True, blank=True, verbose_name='درباره')
    terms = models.TextField(default='قوانین استفاده از وبسایت...', null=True, blank=True, verbose_name='قوانین')
    email = models.EmailField(default='info@site.com', null=True, blank=True, validators=[EmailValidator], verbose_name="ایمیل")
    phone = models.CharField(max_length=30, default='+98 021 123456', null=True, blank=True, verbose_name="شماره تماس")
    addr = models.CharField(max_length=1000, null=True, blank=True, default="تهران - سید خندان - واحد 2", verbose_name='آدرس')
    slug = models.SlugField(default='about-us', verbose_name="نشانک")
    parent_setting = models.OneToOneField(GeneralSetting, on_delete=models.CASCADE, verbose_name="زیرمجموعه تنظیمات")


    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return "درباره ما"

    def get_absolute_url(self):
        return reverse('home:aboutus-setting', args=(self.slug, ))

    def clean(self):
        validate_only_one_instance(self)


class ContactUsSetting(models.Model):
    contact_us = models.TextField(default='متن تماس با ما', null=True, blank=True, verbose_name='تماس با ما')
    slug = models.SlugField(default='contact-us', verbose_name="نشانک")
    parent_setting = models.OneToOneField(GeneralSetting, on_delete=models.CASCADE, verbose_name="زیرمجموعه تنظیمات")


    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    def __str__(self):
        return 'تماس با ما'

    def get_absolute_url(self):
        return reverse('home:contactus-setting', args=(self.slug, ))

    def clean(self):
        validate_only_one_instance(self)