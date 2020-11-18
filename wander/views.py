from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Attraction, Place, PosterEvent, Restaurant, City


def favourites(request):
    return render(request, 'wander/favourites.html')


def posters(request):
    return render(request, 'wander/posters.html')


def rating(request):
    return render(request, 'wander/rating.html')


def restaurants(request):
    return render(request, 'wander/restaurants.html')


def settings(request):
    return render(request, 'wander/settings.html')
