from . import views

from django.urls import path, include
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpUser.as_view(), name='signup'),
    path('signin/',views.SignInUser.as_view(), name ="signin"),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('change/', views.ChangeUserView.as_view(), name='change'),
    path('test/', views.TestView.as_view(template_name='users/test.html'), name='test'),
    path('favpost/<int:id>/', views.favourite_add_poster, name='favourite_add_poster'),
    path('favrest/<int:id>/', views.favourite_add_restaurant, name='favourite_add_restaurant'),
    path('favattr/<int:id>/', views.favourite_add_attraction, name='favourite_add_attraction'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),

]
