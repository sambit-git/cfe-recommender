from django.urls import path

from movies import app_name

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('all/', MovieListView.as_view(), name="all"),
    path('<int:pk>/', MovieDetailView.as_view(), name="detail"),
]
