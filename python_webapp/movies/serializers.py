from rest_framework import serializers
from .models import Movies, Genre, RatingProvider


class MovieSerializer(serializers.ModelSerializer):
    # Custom field for handling date format
    released = serializers.DateField(format='%d %b %Y', input_formats=['%d %b %Y'])
    dvd = serializers.DateField(format='%d %b %Y', input_formats=['%d %b %Y'])

    class Meta:
        model = Movies
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingProvider
        fields = '__all__'

