from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

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
def movies_list(request):
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()
    movies = response.get('results')

    result = []
    for movie in movies:
        movie_dict = {
            'model': 'movies.movie',
            'pk': movie.get('id'),
            'fields': {
                'movie_id': movie.get('id'),
                'title': movie.get('title'),
                'poster_path': movie.get('poster_path'),
                'overview': movie.get('overview'),
                'vote_average': movie.get('vote_average'),
            }
        }
        result.append(movie_dict)
    print(result)
    
    with open('data.json', 'w', encoding="UTF-8") as make_file:
        json.dump(result, make_file, ensure_ascii=False, indent="\t")

    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)