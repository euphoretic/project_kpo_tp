from django.contrib import admin
from . import views
from django.urls import path, include

app_name = 'users'
urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),

]