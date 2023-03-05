from django.urls import path
from .views import services_view

urlpatterns = [
    path('xidmetlerimiz/', services_view, name='services'),
]