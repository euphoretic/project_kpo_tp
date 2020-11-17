from django.contrib import admin
from . import views
from django.contrib.auth import views as _views
from django.urls import path, include

app_name = 'users'
urlpatterns = [

    # path('register', views.register, name='register'),
    path('signin/', views.user_signin, name='signin'),
    path('signup/', views.user_signup, name='signup'),

]
