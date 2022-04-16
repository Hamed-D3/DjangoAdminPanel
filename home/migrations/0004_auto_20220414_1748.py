# Generated by Django 3.2.12 on 2022-04-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_generalsetting_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutussetting',
            name='slug',
            field=models.SlugField(default='about-us', verbose_name='نشانک'),
        ),
        migrations.AddField(
            model_name='contactussetting',
            name='slug',
            field=models.SlugField(default='contact-us', verbose_name='نشانک'),
        ),
        migrations.AddField(
            model_name='websitesetting',
            name='slug',
            field=models.SlugField(default='general-setting', verbose_name='نشانک'),
        ),
    ]