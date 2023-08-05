from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('movies/', views.movies_scores, name='movies_list'),
    path('series/', views.series_scores, name='series_list'),
    path('games/', views.games_scores, name='games_list')
]