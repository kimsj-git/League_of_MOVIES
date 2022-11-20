from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# 인증된 경우만 허용하도록 권한 부여하는 decorator
# 주석 해제 후 원하는 기능에 @permission_classes([IsAuthenticated]) 추가해주면 됨!

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, MatchListSerializer, MatchSerializer
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
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def match_list(request):
    matches = get_list_or_404(Match)
    serializer = MatchListSerializer(matches, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def match_detail(request, match_pk):
    match = get_object_or_404(Match)
    serializer = MatchSerializer(match, pk=match_pk)
    return Response(serializer.data)