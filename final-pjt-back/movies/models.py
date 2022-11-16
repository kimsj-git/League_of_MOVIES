from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    vote_average = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.title
    