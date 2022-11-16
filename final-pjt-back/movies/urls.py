from django.urls import path, include
from . import views

urlpatterns = [
    path('tmdb/toprated', views.get_top_rated),
]