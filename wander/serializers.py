from rest_framework import serializers

from .models import Attraction, Restaurant, PosterEvent


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attraction
        fields = ('place', 'history', 'status', 'image')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('place', 'name', 'description', 'status',
                  'image')


class PosterEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PosterEvent
        fields = ('place', 'name', 'date_start', 'date_end',
                  'ended', 'status', 'image')
