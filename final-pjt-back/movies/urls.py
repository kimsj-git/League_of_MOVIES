from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.movies_list),
]