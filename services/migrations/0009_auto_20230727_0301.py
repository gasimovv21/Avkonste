# Generated by Django 2.2.19 on 2023-07-27 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_subservicedetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subservicedetail',
            old_name='image',
            new_name='images',
        ),
    ]
