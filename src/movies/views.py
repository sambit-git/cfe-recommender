from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
class MovieListView(ListView):
    paginate_by = 100
    queryset = Movie.objects.all().order_by("-rating_avg")

class MovieDetailView(DetailView):
    queryset = Movie.objects.all()