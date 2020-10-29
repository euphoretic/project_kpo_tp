from django.shortcuts import render


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
