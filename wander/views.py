from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from rest_framework import viewsets

from .models import Attraction, Place, PosterEvent, Restaurant, City
from .serializers import AttractionSerializer, RestaurantSerializer, \
    PosterEventSerializer, CitySerializer, PlaceSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all().order_by('place__name')
    serializer_class = AttractionSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer


class PosterEventViewSet(viewsets.ModelViewSet):
    queryset = PosterEvent.objects.all()
    serializer_class = PosterEventSerializer


'''
class PosterEventListView(generic.ListView):
    model = PosterEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PosterEventDetailView(generic.DetailView):
    model = PosterEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# def poster_single(request, poster):
#
#     poster = get_object_or_404(PosterEvent, slug=poster, status='opened')
#
#     fav = bool
#
#     if poster.favourites.filter(id=request.user.id).exists():
#         fav = True
#
#     return render(request, 'posterevent_detail.html', {'object': poster,  'fav': fav})


class RestaurantListView(generic.ListView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class RestaurantDetailView(generic.DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AttractionListView(generic.ListView):
    model = Attraction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AttractionDetailView(generic.DetailView):
    model = Attraction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def rating(request):
    return render(request, 'wander/rating.html')


def settings(request):
    return render(request, 'wander/settings.html')


def home(request):
    all_poster = PosterEvent.newmanager.all()
    all_restaurant = Restaurant.newmanager.all()
    all_attractions = Attraction.newmanager.all()
    return render(request, 'wander/index.html',
                  {'poster': all_poster, 'restaurant': all_restaurant, 'attraction': all_attractions})

'''
