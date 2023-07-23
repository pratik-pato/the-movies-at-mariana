from django.urls import path
from .views import MovieListCreateAPIView, MovieDetailAPIView
from .views import GenreListCreateAPIView, GenreDetailAPIView
from .views import RatingProviderListCreateAPIView, RatingProviderDetailAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('rating-providers/', RatingProviderListCreateAPIView.as_view(), name='rating-provider-list-create'),
    path('rating-providers/<int:pk>/', RatingProviderDetailAPIView.as_view(), name='rating-provider-detail'),
]
