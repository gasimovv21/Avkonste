from django.db import models

class AboutImages(models.Model):
    firstupfront = models.ImageField(
        verbose_name='Yuxarıdakı 1 ci şekilin üz terefi',
        upload_to='firstUp/front',
    )
    firstupback = models.ImageField(
        verbose_name='Yuxarıdakı 1 ci şekilin alt terefi',
        upload_to='firstUp/back',
    )
    secondupfront = models.ImageField(
        verbose_name='Yuxarıdakı 2 ci şekilin üz terefi',
        upload_to='secondUp/front',
    )
    secondupback = models.ImageField(
        verbose_name='Yuxarıdakı 2 ci şekilin alt terefi',
        upload_to='secondUp/back',
    )
    firstdownfront = models.ImageField(
        verbose_name='Aşağıdaki 1 ci şekilin üz terefi',
        upload_to='firstDown/front',
    )
    firstdownback = models.ImageField(
        verbose_name='Aşağıdaki 1 ci şekilin alt terefi',
        upload_to='firstDown/back',
    )
    seconddownfront = models.ImageField(
        verbose_name='Aşağıdaki 2 ci şekilin üz terefi',
        upload_to='secondDown/front',
    )
    seconddownback = models.ImageField(
        verbose_name='Aşağıdaki 2 ci şekilin alt terefi',
        upload_to='secondDown/back',
    )
    

    class Meta:
        verbose_name = 'Haqqımızda səhifəsinin şəkilləri'
        verbose_name_plural = 'Haqqımızda səhifəsinin şəkilləri'