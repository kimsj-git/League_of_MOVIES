from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# 인증된 경우만 허용하도록 권한 부여하는 decorator
# 주석 해제 후 원하는 기능에 @permission_classes([IsAuthenticated]) 추가해주면 됨!

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from .serializers import MovieListSerializer, MovieSerializer, MatchListSerializer, MatchSerializer, CommentSerializer
from .models import Movie, Match, Comment

import requests

import os
import json

BASE_URL = 'https://api.themoviedb.org/3'

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.load(f)

API_KEY = secrets["API_KEY"]

# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.pk).exists():
            is_liked = True
        else:
            is_liked =False
    elif request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True
    
    serializer = MovieSerializer(movie)
    movie_json = serializer.data
    like_data = {
        "is_liked": is_liked,
    }
    movie_json.update(like_data)
    return Response(movie_json)


@api_view(['GET'])
def match_list(request):
    if request.method == 'GET':
        matches = get_list_or_404(Match)
        serializer = MatchListSerializer(matches, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serialzier = MatchSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET'])
def match_detail(request, match_pk):
    match = get_object_or_404(Match, pk=match_pk)
    serializer = MatchSerializer(match)
    return Response(serializer.data)


@api_view(['POST'])
def match_vote(request, match_pk, movie_pk):
    match = get_object_or_404(Match, pk=match_pk)
    voted_movie = get_object_or_404(Movie, pk=movie_pk)
    if voted_movie == match.movie_1:
        against_movie = match.movie_2
    elif voted_movie == match.movie_2:
        against_movie = match.movie_1
    
    if match.movie_1.movie_id == movie_pk:
        match.movie_1_voters.add(request.user.pk)


# @api_view(['GET'])
# def comment_list(request, match_pk):
#     comments = Comment.objects.filter(match=Match.objects.get(pk=match_pk))
#     print(comments)

#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, match_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, match_pk, movie_pk):
    match = get_object_or_404(Match, pk=match_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(match=match)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)