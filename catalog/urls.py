from django.urls import path
from .views import get_tags_and_subservices

urlpatterns = [
    path('katalog/', get_tags_and_subservices, name='catalog'),
]