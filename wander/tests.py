import datetime

from django.test import TestCase
from django.utils import timezone

from .models import PosterEvent


class PosterEventModelTests(TestCase):

    def test_ended_in_past_poster_event(self):
        """ was_ended() возвращает False для событий, которые ещё не закончились """
        time_start = timezone.now() - datetime.timedelta(days=30)
        time_end = timezone.now() - datetime.timedelta(days=29)
        past_poster_event = PosterEvent(date_start=time_start, date_end=time_end)
        past_poster_event.mark_ended()
        # print(past_poster_event.ended)
        self.assertIs(past_poster_event.was_ended(), True)

    def test_date_start_later_then_date_end(self):
        """ Начало мероприятия установленно позже чем его конец. Мероприятие закончится раньше, чем начнется"""
        time_start = timezone.now() + datetime.timedelta(days=30)
        time_end = timezone.now() - datetime.timedelta(days=30)
        future_poster_event = PosterEvent(date_start=time_start, date_end=time_end)
        # future_poster_event.is_date_correct()
        self.assertIs(future_poster_event.is_date_correct(), False)

    # def test_was_published_recently_with_future_question(self):
    #     """
    #     was_published_recently() возвращает False для мероприятий у которых
    #     is in the future.
    #     """
    #     time = timezone.now() + datetime.timedelta(days=30)
    #     future_question = Question(pub_date=time)
    #     self.assertIs(future_question.was_published_recently(), False)


