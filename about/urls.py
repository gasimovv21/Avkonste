from django.urls import path
from .views import about_view

urlpatterns = [
    path('haqqımızda/', about_view, name='about'),
]