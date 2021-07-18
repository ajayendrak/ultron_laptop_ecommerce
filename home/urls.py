from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('test', views.test, name='test'),
    path('contactus', views.contactus, name='contactus'),
]
