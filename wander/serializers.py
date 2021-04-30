from rest_framework import serializers

from .models import Attraction, Restaurant, PosterEvent, City, Place


class AttractionSerializer(serializers.ModelSerializer):
    place_id = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(),
                                                  source='place.id')

    class Meta:
        model = Attraction
        fields = ['id', 'history', 'status', 'image', 'place_id', 'favourites']


class RestaurantSerializer(serializers.ModelSerializer):
    place_id = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(),
                                                  source='place.id')

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'status',
                  'image', 'place_id', 'favourites']


class PosterEventSerializer(serializers.ModelSerializer):
    place_id = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(),
                                                  source='place.id')

    class Meta:
        model = PosterEvent
        fields = ['id', 'name', 'date_start', 'date_end',
                  'ended', 'status', 'image', 'place_id', 'favourites']


class PlaceSerializer(serializers.ModelSerializer):
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(),
                                                 source='city.id')
    attraction = AttractionSerializer(many=True, read_only=True)
    restaurant = RestaurantSerializer(many=True, read_only=True)
    posterEvent = PosterEventSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'full_address', 'name', 'description',
                  'image_map', 'city_id', 'attraction', 'restaurant', 'posterEvent']

    def create(self, validated_data):
        subject = Place.objects.create(city=validated_data['city']['id'],
                                       name=validated_data['name'])
        return subject


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name', ]
