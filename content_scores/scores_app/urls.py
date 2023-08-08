from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from . import views

router = routers.DefaultRouter()
router.register(r'Content', ContentViewSet)
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('movies/', views.movies_scores, name='movies_list'),
    path('series/', views.series_scores, name='series_list'),
    path('games/', views.games_scores, name='games_list'),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]