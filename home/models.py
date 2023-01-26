from django.db import models
from django.core.exceptions import ValidationError

class HomeSlideshow(models.Model):
    image = models.ImageField(
        verbose_name='Ana səhifənin Slaydşousu üçün şəkillər',
        upload_to='home_slideshow_images'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Ana səhifənin Slaydşou üçün şəkil'
        verbose_name_plural = 'Ana səhifənin Slaydşou üçün şəkillər'

    def save(self, *args, **kwargs):
        if self.pk is None and HomeSlideshow.objects.count() >= 5:
            raise ValidationError("Maksimum görüntü Sayına Çatdı. Zəhmət olmasa yenilərini yükləmədən əvvəl mövcud şəkilləri silin")
        super(HomeSlideshow, self).save(*args, **kwargs)


class HomeServiceOne(models.Model):
    image = models.ImageField(
        verbose_name='Ana səhifənin Xidmət 1 üçün şəkil',
        upload_to='home_service1_images',
    )
    title = models.TextField(verbose_name='Ana səhifənin Xidmət 1 üçün başlıq',
                            help_text='Ana səhifənin 1 Xidmət üçün başlıqi əlavə edin!')
    text = models.TextField(verbose_name='Ana səhifənin Xidmət 1 üçün mətn',
                            help_text='Ana səhifənin 1 Xidmət üçün mətnini əlavə edin!')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Ana səhifənin Xidmət 1-in məlumati'
        verbose_name_plural = 'Ana səhifənin Xidmət 1-in məlumati'


class HomeServiceTwo(models.Model):
    image = models.ImageField(
        verbose_name='Ana səhifənin Xidmət 2 üçün şəkil',
        upload_to='home_service2_images'
    )
    title = models.TextField(verbose_name='Ana səhifənin Xidmət 2 üçün başlıq',
                            help_text='Ana səhifənin 2 Xidmət üçün başlıqi əlavə edin!')
    text = models.TextField(verbose_name='Ana səhifənin 2 üçün mətn',
                            help_text='Ana səhifənin 1 Xidmət üçün mətnini əlavə edin!')
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'Ana səhifənin Xidmət 2-in məlumati'
        verbose_name_plural = 'Ana səhifənin Xidmət 2-in məlumati'


class HomeServiceThird(models.Model):
    image = models.ImageField(
        verbose_name='Ana səhifənin Xidmət 3 üçün şəkil',
        upload_to='home_service3_images'
    )
    title = models.TextField(verbose_name='Ana səhifənin Xidmət 3 üçün başlıq',
                            help_text='Ana səhifənin 3 Xidmət üçün başlıqi əlavə edin!')
    text = models.TextField(verbose_name='Ana səhifənin Xidmət 3 üçün mətn',
                            help_text='Ana səhifənin 3 Xidmət üçün mətnini əlavə edin!')
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'Ana səhifənin Xidmət 3-ün məlumati'
        verbose_name_plural = 'Ana səhifənin Xidmət 3-ün məlumati'