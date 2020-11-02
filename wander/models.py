from django.db import models
from django.utils.translation import gettext_lazy as _


class Places(models.Model):
    city = models.ForeignKey('SelectCity', on_delete=models.CASCADE, related_name='city')
    full_address = models.CharField(max_length=150)
    name_place = models.CharField(max_length=50)
    place_rating = models.FloatField(max_length=2)
    description = models.CharField(max_length=120)


class Attractions(Places):
    history = models.CharField(max_length=120)


class Restaurants(Places):
    pass


class Poster(Places):
    date_event_start = models.DateField(auto_now=False, auto_now_add=False, )
    date_event_end = models.DateField(auto_now=False, auto_now_add=False, )
    name_event = models.CharField(max_length=30)



class SelectCity(models.Model):
    CITY_CHEBOKSARY = 'CHE', _('Cheboksary')
    CITY_GUS_KHRUSTALNY = 'GUS', _('Gus-khrustalny')
    __all = (CITY_CHEBOKSARY,
             CITY_GUS_KHRUSTALNY,
             )
    selected_city = models.CharField(max_length=3, choices=__all, default=CITY_CHEBOKSARY)

    def __str__(self):
        return str(self.selected_city)


