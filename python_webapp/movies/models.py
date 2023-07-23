from django.db import models


class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    rated = models.CharField(max_length=20)
    released = models.DateField()
    runtime = models.CharField(max_length=50)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actors = models.TextField()
    plot = models.TextField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    awards = models.TextField()
    poster = models.URLField(default=None, null=True)
    meta_score = models.PositiveIntegerField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_id = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    dvd = models.DateField(default=None, null=True)
    box_office = models.CharField(max_length=100)
    production = models.CharField(max_length=255)
    website = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Movies"


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    class Meta:
        db_table = "Genre"


class RatingProvider(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.source

    class Meta:
        db_table = "RatingProvider"


class MovieGenre(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = "MovieGenre"


class MovieRating(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating_provider = models.ForeignKey(RatingProvider, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.movie.title} - {self.rating_provider.source} - {self.value}"

    class Meta:
        db_table = "MovieRating"

