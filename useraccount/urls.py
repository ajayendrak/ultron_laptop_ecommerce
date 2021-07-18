from django.contrib import admin
from django.urls import path
from useraccount import views

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.sign_up, name='signup'),
]
