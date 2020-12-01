from django.urls import path

from wander.views import PosterEventListView, PosterEventDetailView, RestaurantListView, RestaurantDetailView

urlpatterns = [
    path('', PosterEventListView.as_view(), name='poster-list'),
    path('poster/<int:pk>/', PosterEventDetailView.as_view(), name='poster-detail'),
    # path('favourites', views.favourites, name='favourites'),
    path('posters', PosterEventListView.as_view(), name='poster-list'),
    # path('posters/<int:pk>', views.PosterEventListView.as_view(), name='posters'),
    # path('rating', views.rating, name='rating'),
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    # path('settings', views.settings, name='settings'),
    # path('', views.posters, name='posters'),
    # path('posters', views.posters, name='posters'),
]




