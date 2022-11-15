from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
def movies_list(request):
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()
    movies = response.get('results')
    print(movies[0])
    # return movies

