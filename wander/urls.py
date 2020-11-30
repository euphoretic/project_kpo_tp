from django.urls import path

from wander.views import PosterEventListView, PosterEventDetailView

urlpatterns = [
    path('', PosterEventListView.as_view(), name='poster-list'),
    path('poster/<int:pk>/', PosterEventDetailView.as_view(), name='poster-detail'),
    # path('favourites', views.favourites, name='favourites'),
    # path('posters', views.PosterEventListView, name='poster-list'),
    # path('posters/<int:pk>', views.PosterEventListView.as_view(), name='posters'),
    # path('rating', views.rating, name='rating'),
    # path('restaurants', views.restaurants, name='restaurants'),
    # path('settings', views.settings, name='settings'),
    # path('', views.posters, name='posters'),
    # path('posters', views.posters, name='posters'),
]




