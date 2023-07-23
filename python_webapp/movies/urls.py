from django.urls import path
from .views import MovieListCreateAPIView, MovieDetailAPIView
from .views import GenreListCreateAPIView, GenreDetailAPIView
from .views import RatingProviderListCreateAPIView, RatingProviderDetailAPIView
from .views import MovieGenreListCreateAPIView, MovieGenreDetailAPIView
from .views import MovieRatingListCreateAPIView, MovieRatingDetailAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('rating-providers/', RatingProviderListCreateAPIView.as_view(), name='rating-provider-list-create'),
    path('rating-providers/<int:pk>/', RatingProviderDetailAPIView.as_view(), name='rating-provider-detail'),
    path('movie-genres/', MovieGenreListCreateAPIView.as_view(), name='movie-genre-list-create'),
    path('movie-genres/<int:pk>/', MovieGenreDetailAPIView.as_view(), name='movie-genre-detail'),
    path('movie-ratings/', MovieRatingListCreateAPIView.as_view(), name='movie-rating-list-create'),
    path('movie-ratings/<int:pk>/', MovieRatingDetailAPIView.as_view(), name='movie-rating-detail'),
]
