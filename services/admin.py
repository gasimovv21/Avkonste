from django.contrib import admin
from .models import Services, SubService


class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 0
    fields = ('image','title', 'text')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'tag','text',)
    search_fields = ('tag',)
    list_filter = ('id',)
    empty_value_display = '-boş-'
    inlines = [SubServiceInline]
