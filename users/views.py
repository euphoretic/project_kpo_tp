from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, update_session_auth_hash, get_user_model
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm

class SignUpUser(CreateView):
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, 'users/signup.html', {'title': 'Регистрация - Wander', 'form': SignUpForm()})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
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
            return redirect('/')
        return render(request, 'users/signin.html', {'title': 'Вход - Wander','form': form})
