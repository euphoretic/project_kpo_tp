import json

from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone
from django.views import View, generic
from django.http import HttpResponse


def register(request):
    """registration new user """
    if request.method != 'POST':
        # show empty form
        form = UserCreationForm()
    else:
        # show not empty form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            # login, to homepage
            login(request, new_user)
            return redirect('')


def user_signin(request):
    if request.method == 'POST':
        return render(request, 'users/user_signin.html')
        # form = LoginForm(data=)
    return render(request, 'users/user_signin.html')


# изменить по типу registration
def user_signup(request):
    if request.method == 'POST':
        return render(request, 'users/user_signup.html')
        # form = LoginForm(data=)
    return render(request, 'users/user_signup.html')


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
