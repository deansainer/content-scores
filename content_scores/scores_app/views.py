from django.shortcuts import render
from .models import *


def home_page(request):
    context = {}
    return render(request, 'scores_app/home_page.html', context)
def movies_scores(request):
    movies_list = Content.objects.all().filter(content_type=2)
    context = {'movies_list': movies_list}
    return render(request, 'scores_app/movies_scores.html', context)

def series_scores(request):
    series_list = Content.objects.all().filter(content_type=3)
    context = {'series_list': series_list}
    return render(request, 'scores_app/series_scores.html', context)

def games_scores(request):
    games_list = Content.objects.all().filter(content_type=1)
    context = {'games_list': games_list}
    return render(request, 'scores_app/games_scores.html', context)

