# Generated by Django 2.2.19 on 2023-03-07 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20230124_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='tag',
            field=models.TextField(default=True, help_text='Xidmət üçün qisa başlıqi əlavə edin!', max_length=16, verbose_name='Xidmət üçün qisa başlıq'),
        ),
    ]