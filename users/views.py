import json

from django.views import View, generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login, authenticate, logout, get_user, update_session_auth_hash
from django.views.generic import CreateView

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import SignUpForm

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
        form = AuthenticationForm()
        return render_to_response('/', {'form': form}, context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                return render_to_response('/', {'form': form}, context_instance=RequestContext(request))
        else: return render_to_response('/', {'form': form}, context_instance=RequestContext(request))
#template = loader.get_template('wander/base_new.html')   context = {'form': form}
class SignOutView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

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

class FavoritesView(View):
    model = None

    def post(self, request, pk):
        user = get_user(request)
        favorites, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        if not created:
            favorites.delete()

        return HttpResponse(
           json.dump({
               "result": created,
               "count": self.model.objects.filter(obj_id=pk).count()
           }),
           content_type="application/json"
        )
