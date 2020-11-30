from . import views

from django.urls import path, include
from django.contrib.auth.decorators import login_required
from users.models import FavoritesAttraction, FavoritesPosterEvent, FavoritesRestaurant

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpUser.as_view(template_name='users/signup.html'), name='signup'),
    path('signin/', views.SignInUser.as_view(template_name='users/signin.html'), name='signin'),
    path('favorites/attraction',
         login_required(views.FavoritesView.as_view(model=FavoritesAttraction)), name='favorites_attraction'),
    path('favorites/restaurant',
         login_required(views.FavoritesView.as_view(model=FavoritesRestaurant)), name='favorites_restaurant'),
    path('favorites/event',
         login_required(views.FavoritesView.as_view(model=FavoritesPosterEvent)), name='favorites_poster_event'),

]
