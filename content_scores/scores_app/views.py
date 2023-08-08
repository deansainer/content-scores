from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *

def home_page(request):
    context = {}
    return render(request, 'scores_app/home_page.html', context)
def movies_scores(request):
    movies_list = Content.objects.filter(content_type=2).order_by('score')[::-1]
    list_length = len(movies_list)
    context = {'movies_list': movies_list, 'list_length': list_length}
    return render(request, 'scores_app/movies_scores.html', context)

def series_scores(request):
    series_list = Content.objects.filter(content_type=3).order_by('score')[::-1]
    list_length = len(series_list)
    context = {'series_list': series_list, 'list_length': list_length}
    return render(request, 'scores_app/series_scores.html', context)

def games_scores(request):
    games_list = Content.objects.filter(content_type=1).order_by('score')[::-1]
    list_length = Content.objects.filter(content_type=1).order_by('score')[::-1]
    context = {'games_list': games_list, 'list_length': list_length}
    return render(request, 'scores_app/games_scores.html', context)

class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)