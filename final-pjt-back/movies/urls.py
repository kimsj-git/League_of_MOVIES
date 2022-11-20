from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('league/', views.match_list),
    path('league/<int:match_pk>/', views.match_detail),
    # path('league/<int:match_pk>/<int:movie_pk>/', views.match_vote),
    # path('league/<int:match_pk>/comments/', views.comment_list),
    path('league/<int:match_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path('league/<int:match_pk>/comments/<int:movie_pk>/', views.comment_create),

    # path('tmdb/toprated', views.get_top_rated),
]