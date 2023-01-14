from rest_framework import serializers
from .models import Location, Item, VideosDetails, UserDetails


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')



class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideosDetails
        fields = ('__all__')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('__all__')