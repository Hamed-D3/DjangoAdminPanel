# Generated by Django 3.2.12 on 2022-04-07 22:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator('^(0098|\\+?98|0)9\\d{9}$', message='لطفا شماره موبایل معتبر وارد نمایید')], verbose_name='شماره موبایل'),
        ),
    ]
