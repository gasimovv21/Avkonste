from django.db import models

class Services(models.Model):
    image = models.ImageField(
        verbose_name='Xidmət üçün şəkil',
        upload_to='services_images',
    )
    title = models.TextField(verbose_name='Xidmət üçün başlıq',
                            help_text='Xidmət üçün başlıqi əlavə edin!')
    text = models.TextField(verbose_name='Xidmət üçün mətn',
                            help_text='Xidmət üçün mətnini əlavə edin!')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Xidmət-in məlumati'
        verbose_name_plural = 'Xidmət-in məlumati'