from django.urls import path
from . import views

urlpatterns = [
    path('katalog/', views.get_tags_and_subservices, name='catalog'),
    path('katalog/<int:pk>/', views.sub_services_detail, name='subservice_detail'),



    path('catalog/all/', views.get_all_subservices, name='all_subservices'),
    path('catalog/<int:services_id>/', views.get_subservices, name='get_subservices')
]