from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies, Genre, RatingProvider, MovieGenre, MovieRating
from .serializers import MovieSerializer, GenreSerializer, RatingProviderSerializer,\
    MovieGenreSerializer, MovieRatingSerializer, MovieSerializerAll, MovieRatingValidationSerializer


class MovieListCreateAPIView(APIView):
    def get(self, request):
        movies = Movies.objects.prefetch_related('moviegenre_set__genre', 'movierating_set__rating_provider').all()

        serializer = MovieSerializerAll(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response("Movie not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreListCreateAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response("Genre not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RatingProviderListCreateAPIView(APIView):
    def get(self, request):
        providers = RatingProvider.objects.all()
        serializer = RatingProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingProviderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return RatingProvider.objects.get(pk=pk)
        except RatingProvider.DoesNotExist:
            return Response("Rating provider not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        provider = self.get_object(pk)
        serializer = RatingProviderSerializer(provider)
        return Response(serializer.data)

    def put(self, request, pk):
        provider = self.get_object(pk)
        serializer = RatingProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        provider = self.get_object(pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieGenreListCreateAPIView(APIView):
    def get(self, request):
        genres = MovieGenre.objects.all()
        serializer = MovieGenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieGenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieGenreDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MovieGenre.objects.get(pk=pk)
        except MovieGenre.DoesNotExist:
            return Response("Movie genre not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = MovieGenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = MovieGenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieRatingListCreateAPIView(APIView):
    def get(self, request):
        ratings = MovieRating.objects.all()
        serializer = MovieRatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieRatingValidationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieRatingDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MovieRating.objects.get(pk=pk)
        except MovieRating.DoesNotExist:
            return Response("Movie rating not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        rating = self.get_object(pk)
        serializer = MovieRatingSerializer(rating)
        return Response(serializer.data)

    def put(self, request, pk):
        rating = self.get_object(pk)
        serializer = MovieRatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rating = self.get_object(pk)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)