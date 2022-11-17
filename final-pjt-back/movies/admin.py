from django.contrib import admin
from .models import Movie, Genre, Match, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Match)
admin.site.register(Comment)