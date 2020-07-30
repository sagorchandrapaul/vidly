from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Movie
from .forms import CreateMovie, CreateGenre


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    if request.method == "POST":
        form = CreateMovie(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('/movies/', pk=movie.id)
    else:
        form = CreateMovie()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


def genres(request):
    if request.method == "POST":
        form = CreateGenre(request.POST)
        if form.is_valid():
            thriller = form.save(commit=False)
            thriller.save()
            return redirect('/movies/', pk=thriller.id)
    else:
        form = CreateGenre()
    context = {
        'form': form
    }
    return render(request, 'movies/createGenre.html', context)