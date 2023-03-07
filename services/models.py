from django.db import models

class Services(models.Model):
    image = models.ImageField(
        verbose_name='Xidmət üçün şəkil',
        upload_to='services_images',
    )
    title = models.TextField(verbose_name='Xidmət üçün başlıq',
                            help_text='Xidmət üçün başlıqi əlavə edin!')
    tag = models.TextField(verbose_name='Xidmət üçün qisa başlıq',
                        max_length=16,
                        help_text='Xidmət üçün qisa başlıqi əlavə edin!')
    text = models.TextField(verbose_name='Xidmət üçün mətn',
                            help_text='Xidmət üçün mətnini əlavə edin!')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmətlər'


class SubService(models.Model):
    image = models.ImageField(
        verbose_name='Sub-service üçün şəkil',
        upload_to='subservices_images',
        default=True,
    )
    title = models.TextField(
        verbose_name='Sub-service üçün başlıq',
        help_text='Sub-service üçün başlıqi əlavə edin!'
    )
    text = models.TextField(
        verbose_name='Sub-service üçün mətn',
        help_text='Sub-service üçün mətnini əlavə edin!'
    )
    service = models.ForeignKey(
        Services,
        on_delete=models.CASCADE,
        related_name='subservices',
        verbose_name='Ana xidmət',
        help_text='Ana xidməti seçin'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Sub-xidmət'
        verbose_name_plural = 'Sub-xidmətlər'