import datetime
from django.utils import timezone
from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

def image_path_attraction(instance, filename):
    return 'img/attraction_{0}_{1}'.format(instance.id, filename)

def image_path_restaurant(instance, filename):
    return 'img/restaurant_{0}_{1}'.format(instance.id, filename)

def image_path_posterevent(instance, filename):
    return 'img/posterevent_{0}_{1}'.format(instance.id, filename)

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
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='opened')

    options = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE, )
    history = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=options, default='opened')
    favourites = models.ManyToManyField(
        User, related_name='favourite_attraction', default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    image = models.ImageField(upload_to=image_path_attraction, default='img/default.jpg')

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new Attraction!')
        else:
            print('Updating the existing one')
        super(Attraction, self).save(**kwargs)

    def __str__(self):
        return "%s the attraction" % self.place.name


class Restaurant(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='opened')

    options = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=options, default='opened')
    favourites = models.ManyToManyField(
        User, related_name='favourite_restaurant', default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    image = models.ImageField(upload_to=image_path_restaurant, default='img/default.jpg')

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

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='opened')

    options = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    date_end = models.DateField(auto_now=False, auto_now_add=False, default=None, null=True)
    name = models.CharField(max_length=30, default='add_name_event')
    ended = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=options, default='opened')
    favourites = models.ManyToManyField(
        User, related_name='favourite_poster_event', default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    image = models.ImageField(upload_to=image_path_posterevent, default='img/default.jpg')

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
