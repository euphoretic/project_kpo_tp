import json

from django.views import View, generic
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, get_user, update_session_auth_hash
from django.views.generic import CreateView
from .forms import SignUpForm
from wander.models import Restaurant, PosterEvent, Attraction


@ login_required
def favourite_list(request):
    new_poster_event = PosterEvent.newmanager.filter(favourites=request.user)
    new_restaurant = Restaurant.newmanager.filter(favourites=request.user)
    new_attraction = Attraction.newmanager.filter(favourites=request.user)
    return render(request,
                  'users/favourites.html',
                  {'new_poster_event': new_poster_event,
                   'new_restaurant': new_restaurant,
                   'new_attraction': new_attraction})


@ login_required
def favourite_add_poster(request, id):
    post = get_object_or_404(PosterEvent, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@ login_required
def favourite_add_attraction(request, id):
    post = get_object_or_404(Attraction, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@ login_required
def favourite_add_restaurant(request, id):
    post = get_object_or_404(Restaurant, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class SignUpUser(CreateView):
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, 'users/signup.html', {'title': 'Регистрация - Wander', 'form': SignUpForm()})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users/test') # temp, redirect('/')
        return render(request, 'users/signup.html', {'title': 'Регистрация - Wander', 'form': form})


class SignInUser(CreateView):
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        return render(request, 'users/signin.html', {'title': 'Вход - Wander', 'form': AuthenticationForm()})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users/test') # temp, redirect('/')
        return render(request, 'users/signin.html', {'title': 'Вход - Wander','form': form})


class SignOutView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/users/test') # temp, redirect('/')


class ChangeUserView(CreateView):
    form_class = PasswordChangeForm

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, 'users/change.html', {'title':'Смена пароля - Wander', 'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/users/test') # temp, redirect('/')
        return render(request, 'users/change.html', {'title':'Смена пароля - Wander', 'form': form})


class TestView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/test.html', {'title':'Тест авторизации - Wander'})

