from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# 인증된 경우만 허용하도록 권한 부여하는 decorator
# 주석 해제 후 원하는 기능에 @permission_classes([IsAuthenticated]) 추가해주면 됨!

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.db.models import Q
from .serializers import MovieListSerializer, MovieSerializer, MatchListSerializer, MatchSerializer, CommentSerializer, MovieDetailSerializer
from .models import Movie, Match, Comment

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
    serializer = MovieDetailSerializer(movie)
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


@api_view(['GET', 'POST'])
def match_list(request):
    if request.method == 'GET':
        matches = get_list_or_404(Match)
        serializer = MatchListSerializer(matches, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # movie_1, movie_2 조합이 get_list_or_404(Match)에 존재하면 생성 막아야함
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
    movie_1 = match.movie_1
    movie_2 = match.movie_2

    # 해당 매치에서 투표하지 않은 사용자들만 투표 가능
    if match.movie_1_voters.filter(id=request.user.id).count() == 0 and match.movie_2_voters.filter(id=request.user.id).count() == 0:    
        # 입력받은 movie_pk에 해당하는 movie에 대해 투표
        if movie_pk == movie_1.pk:
            match.movie_1_voters.add(request.user)
        elif movie_pk == movie_2.pk:
            match.movie_2_voters.add(request.user)
    # 이미 투표한 사용자
    else:
        print('이미 투표하셨습니다.')
    
    # movie_1, movie_2 각각의 득표수를 비교하여 두 영화의 승패 관계 갱신
    count_1 = match.movie_1_voters.count()  # movie_1 득표수
    count_2 = match.movie_2_voters.count()  # movie_2 득표수
    if count_1 == count_2:

        if movie_1.win_movies.filter(pk=movie_2.pk).exists():
            movie_1.win_movies.remove(movie_2)
        elif movie_2.win_movies.filter(pk=movie_1.pk).exists():
            movie_2.win_movies.remove(movie_1)
    
    elif count_1 > count_2:
        movie_1.win_movies.add(movie_2)
    
    elif count_1 < count_2:
        movie_2.win_movies.add(movie_1)
    
    serializer = MatchSerializer(match)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def comment_list(request, match_pk):
    
    if request.method == 'GET':
        match = get_object_or_404(Match, pk=match_pk)
        comments = Comment.objects.filter(match=match)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = get_user_model().objects.get(pk=request.user.pk)
        match = get_object_or_404(Match, pk=match_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(match=match, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, match_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = get_user_model().objects.get(pk=request.user.pk)
    match = get_object_or_404(Match, pk=match_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(match=match, user=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response('댓글이 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_list_win_rate(request):
    # movies = get_list_or_404(Movie, vote_average__gt=8)
    # 매치에 포함된(Match에서 movie_1 또는 movie_2로 가져왔을 때 비어있지 않은) 영화들을 가져오기
    movies = get_list_or_404(Movie, Q(movie_1__isnull=False) | Q(movie_2__isnull=False))
    movies = list(set(movies))  # 중복 제거

    serializer = MovieListSerializer(movies, many=True)
    json_data = serializer.data
    for data in json_data:
        movie = Movie.objects.get(pk=data['movie_id'])
        match_cnt = movie.movie_1.count() + movie.movie_2.count()
        data['win_rate'] = movie.win_movies.count() / match_cnt
    
    json_data.sort(key=lambda x: [-x.get('win_rate'), -len(x.get('win_movies'))])
    return Response(json_data)