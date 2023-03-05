from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from handlers import handler404, handler403, handler505



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('', include("services.urls")),
    path('', include("about.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
handler403 = handler403
handler505 = handler505
