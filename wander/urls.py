from django.urls import path, include
from django.conf import settings as _settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet, basename='City')
router.register(r'place', views.PlaceViewSet, basename='Place')
router.register(r'attraction', views.AttractionViewSet, basename='Attraction')
router.register(r'poster', views.PosterEventViewSet, basename='PosterEvent')
router.register(r'restaurant', views.RestaurantViewSet, basename='Restaurant')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''
# from wander.views import PosterEventListView, PosterEventDetailView, RestaurantListView, RestaurantDetailView,\
#    AttractionListView, AttractionDetailView, rating, settings, home\

urlpatterns = [
    path('', home, name='homepage'),
    path('poster/', PosterEventListView.as_view(), name='poster-list'),
    path('poster/<int:pk>/', PosterEventDetailView.as_view(), name='poster-detail'),
    path('attraction/', AttractionListView.as_view(), name='attraction-list'),
    path('attraction/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
    path('restaurant/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('rating/', rating, name='rating'),
    path('settings/', settings, name='settings'),
] + static(_settings.MEDIA_URL, document_root=_settings.MEDIA_ROOT)
'''
