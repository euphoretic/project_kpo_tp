from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.name


class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    full_address = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    rating = models.FloatField(max_length=3)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "%s: %s, %s" % (self.name, self.city.__str__(),  self.full_address)


class Attraction(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, )
    history = models.CharField(max_length=255)

    def __str__(self):
        return "%s the attraction" % self.place.name


class Restaurant(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "%s the restaurant" % self.name


class PosterEvent(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, )
    date_start = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    date_end = models.DateField(auto_now=False, auto_now_add=False, default=None, null=True)
    name = models.CharField(max_length=30, default='add_name_event')
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

    def __str__(self):
        return "Event: %s %s " % (self.name, self.place)