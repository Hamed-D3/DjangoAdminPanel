# Generated by Django 3.2.12 on 2022-04-01 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default/user.png', upload_to='avatars/', validators=[django.core.validators.validate_image_file_extension], verbose_name='عکس پروفایل'),
        ),
    ]
