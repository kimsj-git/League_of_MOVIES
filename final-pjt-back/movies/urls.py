from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('league/', views.match_list),
    path('league/<int:match_pk>/', views.match_detail),
    # path('league/<int:match_pk>/<int:movie_pk>/', views.match_vote),
    # path('league/<int:match_pk>/comments/', views.comments),

    # path('tmdb/toprated', views.get_top_rated),
]