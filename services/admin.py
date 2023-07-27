from django.contrib import admin
from .models import Services, SubService, SubServiceDetail, SubServiceDetailImageModel

class SubServiceDetailInline(admin.TabularInline):
    model = SubServiceDetail
    extra = 0
    max_num = 1  # set the maximum number of point lines to 8
    min_num = 0  # set the minimum number of point lines to 8
    fields = ('text',)

class SubServiceInline(admin.TabularInline):
    model = SubService
    extra = 0
    fields = ('image', 'title', 'text')
    inlines = [SubServiceDetailInline]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'tag', 'text',)
    search_fields = ('tag',)
    list_filter = ('id',)
    empty_value_display = '-boş-'
    inlines = [SubServiceInline]

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'text',)
    search_fields = ('title',)
    list_filter = ('id',)
    empty_value_display = '-boş-'
    inlines = [SubServiceDetailInline]

@admin.register(SubServiceDetail)
class SubServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'sub_service',)
    search_fields = ('sub_service__title',)
    list_filter = ('sub_service__title',)
    filter_horizontal = ('images',)  # Используем filter_horizontal для множественного выбора фотографий

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Убираем ограничение на количество выбранных фотографий для существующих объектов
        if obj:
            form.base_fields['images'].queryset = form.base_fields['images'].queryset.model.objects.all()
        return form
    

@admin.register(SubServiceDetailImageModel)
class SubServiceDetailImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)