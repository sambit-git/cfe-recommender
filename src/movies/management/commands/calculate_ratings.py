from django.core.management.base import BaseCommand, CommandParser

from movies.models import Movie
from ratings.models import Rating

from src.ratings.tasks import task_update_movie_ratings

class Command(BaseCommand):    
    def handle(self, *args, **options) -> str | None:
        task_update_movie_ratings()
        