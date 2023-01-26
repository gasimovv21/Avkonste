from django.contrib import admin

from .models import HomeSlideshow, HomeServiceOne, HomeServiceTwo, HomeServiceThird
from django.contrib import messages
from django.http import HttpResponseRedirect




@admin.register(HomeSlideshow)
class HomeSlideshowAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    search_fields = ('image',)
    list_filter = ('id',)
    empty_value_display = '-boş-'

    def save_model(self, request, obj, form, change):
        if HomeSlideshow.objects.count() >= 5 and not change:
            request.show_warning_message = True
        else:
            obj.save()

    def response_add(self, request, obj, post_url_continue=None):
        if hasattr(request, 'show_warning_message') and request.show_warning_message:
            messages.warning(request, "Yalnız 5 şəkil əlavə edə bilərsiniz.")
            del request.show_warning_message
            return HttpResponseRedirect('.')
        else:
            return super().response_add(request, obj, post_url_continue)


@admin.register(HomeServiceOne)
class HomeServiceOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title','text',)
    search_fields = ('title',)
    list_filter = ('id',)
    empty_value_display = '-boş-'


@admin.register(HomeServiceTwo)
class HomeServiceTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title','text',)
    search_fields = ('title',)
    list_filter = ('id',)
    empty_value_display = '-boş-'

@admin.register(HomeServiceThird)
class HomeServiceThirdAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title','text',)
    search_fields = ('title',)
    list_filter = ('id',)
    empty_value_display = '-boş-'