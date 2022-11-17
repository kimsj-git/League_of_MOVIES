import requests
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.load(f)

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = secrets["API_KEY"]


def get_movies_json(path):
    json_data = []
    for page in range(1, 6):
        params = {
            'api_key': API_KEY,
            'region': 'KR',
            'language': 'ko',
            'page': f'{page}',
        }
        response = requests.get(BASE_URL + path, params=params).json()
        movies = response.get('results')

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
                    'genres': movie.get('genre_ids')
                }
            }
            json_data.append(movie_dict)
    
    # JSON 데이터를 생성하기 위한 코드
    with open('data.json', 'w', encoding="UTF-8") as make_file:
        json.dump(json_data, make_file, ensure_ascii=False, indent="\t")


path_top_rated = '/movie/top_rated'
path_popular = '/movie/popular'
path_now_playing = '/movie/now_playing'
path_upcoming = '/movie/upcoming'

# get_movies_json(path_top_rated)


def get_genres_json():
    path = '/genre/movie/list'
    json_data = []
    for page in range(1, 6):
        params = {
            'api_key': API_KEY,
            'region': 'KR',
            'language': 'ko',
        }
        response = requests.get(BASE_URL + path, params=params).json()
        # print(response)
        genres = response.get('genres')

        for genre in genres:
            genre_dict = {
                'model': 'movies.genre',
                'pk': genre.get('id'),
                'fields': {
                    # 'genre_id': genre.get('id'),
                    'name': genre.get('name'),
                }
            }
            json_data.append(genre_dict)
    
    # JSON 데이터를 생성하기 위한 코드
    with open('genres.json', 'w', encoding="UTF-8") as make_file:
        json.dump(json_data, make_file, ensure_ascii=False, indent="\t")


get_genres_json()