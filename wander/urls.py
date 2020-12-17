from django.urls import path

from wander.views import PosterEventListView, PosterEventDetailView, RestaurantListView, RestaurantDetailView,\
    AttractionListView, AttractionDetailView, rating, settings

urlpatterns = [
    path('', PosterEventListView.as_view(), name='poster-list'),
    path('poster/', PosterEventListView.as_view(), name='poster-list'),
    path('poster/<int:pk>/', PosterEventDetailView.as_view(), name='poster-detail'),
    # path('poster/<slug:poster>/', poster_single, name='poster-detail'),
    path('attraction/', AttractionListView.as_view(), name='attraction-list'),
    path('attraction/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('rating/', rating, name='rating'),
    path('settings/', settings, name='settings'),
]




