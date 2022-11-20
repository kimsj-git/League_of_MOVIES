from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# 인증된 경우만 허용하도록 권한 부여하는 decorator
# 주석 해제 후 원하는 기능에 @permission_classes([IsAuthenticated]) 추가해주면 됨!

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
@permission_classes([IsAuthenticated])
def get_top_rated(request):
    path = '/movie/top_rated'
    json_data = []
    return_data = []
    for page in range(1, 6):
        params = {
            'api_key': API_KEY,
            'region': 'KR',
            'language': 'ko',
            'page': f'{page}',
        }
        response = requests.get(BASE_URL + path, params=params).json()
        movies = response.get('results')
        return_data += movies

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
            json_data.append(movie_dict)
    
    # JSON 데이터를 생성하기 위한 코드
    # with open('data.json', 'w', encoding="UTF-8") as make_file:
    #     json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

    serializer = MovieListSerializer(return_data, many=True)
    return Response(serializer.data)