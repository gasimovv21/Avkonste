from django.urls import path
from .views import services_view

urlpatterns = [
    path('xidmətlərimiz/', services_view, name='services'),
]