from rest_framework import serializers
from .models import Movie, Match, Comment
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = '__all__'
    
    like_movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('match', 'user')


class MovieSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('pk', 'user', 'movie_1', 'movie_2', 'movie_1_voters', 'movie_2_voters')


class MatchSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Match
        fields = '__all__'
        read_only_fields = ('user',)


class MovieDetailSerializer(serializers.ModelSerializer):
    class MovieSimpleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Movie
            fields = '__all__'

    comments = CommentSerializer(many=True, read_only=True)
    win_movies = MovieSimpleSerializer(many=True, read_only=True)
    lose_movies = MovieSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'