# Generated by Django 3.2.12 on 2022-04-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalsetting',
            name='deleted_at',
        ),
    ]
