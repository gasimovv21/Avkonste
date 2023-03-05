from django.urls import path
from .views import about_view

urlpatterns = [
    path('haqqimizda/', about_view, name='about'),
]