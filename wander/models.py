from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class SelectCity(models.Model):
    city_for_choice = (
        ('CHE', 'Cheboksary'),
        ('GUS', 'Gus-khrustalny'),
    )
    selected_city = models.CharField(max_length=3, choices=city_for_choice)

    def __str__(self):
        return str(self.selected_city)


class Place(models.Model):
    city = models.ForeignKey(SelectCity, on_delete=models.CASCADE, verbose_name='city')
    full_address = models.CharField(max_length=150)
    name_place = models.CharField(max_length=50)
    place_rating = models.FloatField(max_length=3)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.full_address+' '+self.city.__str__()+' '+self.name_place

    # def save(self, *args, **kwargs):
    #     print('Creating new Place!')
    #     super().save(*args, **kwargs)


class Attraction(Place):
    history = models.CharField(max_length=120)


class Restaurant(Place):
    pass


class PosterEvent(Place):
    date_event_start = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    date_event_end = models.DateField(auto_now=False, auto_now_add=False, default=None, null=True)
    name_event = models.CharField(max_length=30, default='add_name_event')
    ended = models.BooleanField(default=False)

    def mark_ended(self, commit=True):
        self.ended = True
        if commit:
            self.save()

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Event!')
        else:
            print('Updating the existing one')

        super(PosterEvent, self).save(**kwargs)





