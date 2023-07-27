# Generated by Django 2.2.19 on 2023-07-27 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20230307_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=True, upload_to='subservices_images_detail', verbose_name='Sub-service-Ətraflı üçün şəkil')),
                ('text', models.TextField(help_text='Sub-service-Ətraflı üçün mətnini əlavə edin!', verbose_name='Sub-service-Ətraflı üçün mətn')),
                ('sub_service', models.ForeignKey(help_text='Əlaqəli alt xidmət', on_delete=django.db.models.deletion.CASCADE, related_name='details', to='services.SubService', verbose_name='Əlaqəli alt xidmət Ətraflı')),
            ],
            options={
                'verbose_name': 'Ətraflı Əlaqəli alt xidmət',
                'verbose_name_plural': 'Ətraflı Əlaqəli alt xidmət',
                'ordering': ('text',),
            },
        ),
    ]