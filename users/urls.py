from django.contrib import admin
from . import views as users_views
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    path('signup/', users_views.SignUpUser.as_view(template_name='users/signup.html'), name='signup'),
    path('signin/', users_views.SignInUser.as_view(template_name='users/signin.html'), name='signin'),
]
