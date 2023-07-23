from rest_framework import serializers
from .models import Movies, Genre, RatingProvider, MovieGenre, MovieRating


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
        fields = ['genre']


class RatingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingProvider
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'

class RatingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingProvider
        fields = ['source']

class MovieRatingValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = '__all__'

class MovieRatingSerializer(serializers.ModelSerializer):
    rating_provider = RatingProviderSerializer()

    class Meta:
        model = MovieRating
        fields = ['rating_provider', 'value']

class MovieSerializerAll(serializers.ModelSerializer):
    # Custom field for handling date format
    released = serializers.DateField(format='%d %b %Y', input_formats=['%d %b %Y'])
    dvd = serializers.DateField(format='%d %b %Y', input_formats=['%d %b %Y'])

    # Nested serializer for genres
    genres = GenreSerializer(many=True, source='moviegenre_set', read_only=True)

    # Nested serializer for ratings
    ratings = MovieRatingSerializer(many=True, source='movierating_set', read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'