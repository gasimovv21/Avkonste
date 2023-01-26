from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title','text',)
    search_fields = ('title',)
    list_filter = ('id',)
    empty_value_display = '-boş-'
