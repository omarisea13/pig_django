# finegap/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
]
