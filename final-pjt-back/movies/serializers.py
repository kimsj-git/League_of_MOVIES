from rest_framework import serializers
from .models import Movie, Match, Comment

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'overview', 'vote_average', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('match',)


class MovieSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('user', 'movie_1', 'movie_2', 'movie_1_voters', 'movie_2_voters')


class MatchSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    win_movies = MovieListSerializer(many=True, read_only=True)
    lose_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'