# Generated by Django 2.2.19 on 2023-03-07 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20230307_0236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('title',), 'verbose_name': 'Xidmət', 'verbose_name_plural': 'Xidmətler'},
        ),
    ]