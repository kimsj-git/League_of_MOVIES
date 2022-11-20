from rest_framework import serializers
from .models import Movie, Match, Comment

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'overview', 'vote_average')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('user', 'movie_1', 'movie_2', 'movie_1_voters', 'movie_2_voters')


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'