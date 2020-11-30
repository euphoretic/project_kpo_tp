from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from users.models import FavoritesAttraction, FavoritesPosterEvent, FavoritesRestaurant

app_name = 'users'
urlpatterns = [
    path('signin/', views.user_signin, name='signin'),
    path('signup/', views.user_signup, name='signup'),
    path('favorites/attraction',
         login_required(views.FavoritesView.as_view(model=FavoritesAttraction)), name='favorites_attraction'),
    path('favorites/restaurant',
         login_required(views.FavoritesView.as_view(model=FavoritesRestaurant)), name='favorites_restaurant'),
    path('favorites/event',
         login_required(views.FavoritesView.as_view(model=FavoritesPosterEvent)), name='favorites_poster_event'),
]
