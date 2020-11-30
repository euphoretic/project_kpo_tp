from django.test import TestCase
import datetime
from django.utils import timezone

from .models import PosterEvent


class PosterEventModelTests(TestCase):

    def test_ended_with_future_poster_event(self):
        """
        ended() возвращает False для событий, которые ещё не закончились
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_posterevent = PosterEvent()

    def test_date_start_later_then_date_end(self):
        """ Начало мероприятия установленно позже чем его конец.
         Мероприятие закончится раньше, чем начнется"""
        time_start = timezone.now() + datetime.timezone(days=30)
        time_end = timezone.now() - datetime.timezone(days=30)
        future_posterevent = PosterEvent(date_start=time_start, date_end=time_end)
        self.assertIs()

