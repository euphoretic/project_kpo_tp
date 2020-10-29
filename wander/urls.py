from django.urls import path

from . import views

urlpatterns = [
    path('favourites', views.favourites, name='favourites'),
    path('posters', views.posters, name='posters'),
    path('rating', views.rating, name='rating'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('settings', views.settings, name='settings'),
]




