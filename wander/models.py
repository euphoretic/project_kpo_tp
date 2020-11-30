import datetime

from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=20)

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new City!')
        else:
            print('Updating the existing one')
        super(City, self).save(**kwargs)

    def __str__(self):
        return "%s" % self.name


class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    full_address = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    rating = models.FloatField(max_length=3)
    description = models.CharField(max_length=255)

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Place!')
        else:
            print('Updating the existing one')
        super(Place, self).save(**kwargs)

    def __str__(self):
        return "%s: %s, %s" % (self.name, self.city.__str__(),  self.full_address)


class Attraction(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, )
    history = models.CharField(max_length=255)

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Attraction!')
        else:
            print('Updating the existing one')
        super(Attraction, self).save(**kwargs)

    def __str__(self):
        return "%s the attraction" % self.place.name


class Restaurant(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Restaurant!')
        else:
            print('Updating the existing one')
        super(Restaurant, self).save(**kwargs)

    def __str__(self):
        return "%s the restaurant" % self.name


class PosterEvent(models.Model):
    class Meta:
        db_table = "poster_event"

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    date_end = models.DateField(auto_now=False, auto_now_add=False, default=None, null=True)
    name = models.CharField(max_length=30, default='add_name_event')
    ended = models.BooleanField(default=False)

    def mark_ended(self, commit=False):
        if commit or (self.was_ended()):
            self.ended = True
            # self.save()

    def was_ended(self):
        now = timezone.now()
        return (self.date_end < now) or self.ended

    def was_start(self):
        now = timezone.now()
        return (now < self.date_end) and (not self.ended)

    def is_date_correct(self):
        if self.date_end < self.date_start:
            self.date_start, self.date_end = self.date_end, self.date_start
            return False
        return True

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Event!')
        else:
            print('Updating the existing one')
        super(PosterEvent, self).save(**kwargs)

    def __str__(self):
        return "Event: %s %s " % (self.name, self.place)
