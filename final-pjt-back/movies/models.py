from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    vote_average = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self) -> str:
        return self.title


class Match(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_1 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_1')
    movie_2 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_2')
    movie_1_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='voted_movies_1')
    movie_2_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='voted_movies_2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Match: {self.movie_1} vs {self.movie_2}'


class Comment(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    voted_movie = models.BooleanField() # True: movie_1 선택, False: movie_2 선택
    # voted_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content