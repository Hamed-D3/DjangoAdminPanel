# Generated by Django 3.2.12 on 2022-04-02 10:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'تظیمات',
                'verbose_name_plural': 'تظیمات',
            },
        ),
        migrations.CreateModel(
            name='WebSiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='پنل ادمین جنگو', max_length=300, null=True, verbose_name='نام')),
                ('logo', models.ImageField(blank=True, default='default/logo.png', null=True, upload_to='website/', validators=[django.core.validators.validate_image_file_extension], verbose_name='لوگو')),
                ('favico', models.ImageField(blank=True, default='default/ico.png', null=True, upload_to='website/', validators=[django.core.validators.validate_image_file_extension], verbose_name='فیو آیکون')),
                ('url', models.URLField(blank=True, default='http://site.com', null=True, validators=[django.core.validators.URLValidator], verbose_name='آدرس اینترنتی')),
                ('parent_setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.generalsetting', verbose_name='زیرمجموعه تنظیمات')),
            ],
            options={
                'verbose_name': 'عمومی',
                'verbose_name_plural': 'عمومی',
            },
        ),
        migrations.CreateModel(
            name='ContactUsSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us', models.TextField(blank=True, default='متن تماس با ما', null=True, verbose_name='تماس با ما')),
                ('parent_setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.generalsetting', verbose_name='زیرمجموعه تنظیمات')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='AboutUsSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(blank=True, default='درباره ما...', null=True, verbose_name='درباره')),
                ('terms', models.TextField(blank=True, default='قوانین استفاده از وبسایت...', null=True, verbose_name='قوانین')),
                ('email', models.EmailField(blank=True, default='info@site.com', max_length=254, null=True, validators=[django.core.validators.EmailValidator], verbose_name='ایمیل')),
                ('phone', models.CharField(blank=True, default='+98 021 123456', max_length=30, null=True, verbose_name='شماره تماس')),
                ('addr', models.CharField(blank=True, default='تهران - سید خندان - واحد 2', max_length=1000, null=True, verbose_name='آدرس')),
                ('parent_setting', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.generalsetting', verbose_name='زیرمجموعه تنظیمات')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]
