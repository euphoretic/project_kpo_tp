from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from wander.models import Attraction, Restaurant, PosterEvent


class User(AbstractUser):
    @classmethod
    def parse_name(cls, name: str) -> dict:
        if name is None:
            return {}

        parts = name.split('', 2)

        if len(parts) == 1:
            return {'first_name': parts[0]}

        if len(parts) == 2:
            return {'first_name': parts[0], 'last_name': parts[1:]}

        return {'first_name': parts[0], 'last_name': ' '.join(parts[1:])}

    def __str__(self):
        name = self.first_name + ' ' + self.last_name

        if len(name) < 3:
            return self.username

        return name.strip()

    def setattr_and_save(self, key, value):
        """set attribute of the model and save
        there override selected_city, first_name, last_name, favourites_list  """
        setattr(self, key, value)
        self.save()


class FavoritesBase(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class FavoritesAttraction(FavoritesBase):
    class Meta:
        db_table = "favorites_attraction"

    obj = models.ForeignKey(Attraction, verbose_name="Достопримечательность", on_delete=models.CASCADE)


class FavoritesRestaurant(FavoritesBase):
    class Meta:
        db_table = "favorites_restaurant"

    obj = models.ForeignKey(Restaurant, verbose_name="Рестораны", on_delete=models.CASCADE)


class FavoritesPosterEvent(FavoritesBase):
    class Meta:
        db_table = "favorites_poster_event"

    obj = models.ForeignKey(PosterEvent, verbose_name="Мероприятия", on_delete=models.CASCADE)
