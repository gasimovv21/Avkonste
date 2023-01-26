from django.contrib import admin
from .models import AboutImages

@admin.register(AboutImages)
class AboutImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'firstupfront',
        'firstupback',
        'secondupfront',
        'secondupback',
        'firstdownfront',
        'firstdownback',
        'seconddownfront',
        'seconddownback',
    )
    search_fields = ('id',)
    list_filter = ('id',)
    empty_value_display = '-boş-'