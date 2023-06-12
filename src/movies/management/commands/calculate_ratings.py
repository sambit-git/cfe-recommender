from django.core.management.base import BaseCommand, CommandParser

from movies.models import Movie
from ratings.models import Rating

from movies.task import task_claculate_movie_rating

class Command(BaseCommand):
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", nargs="?", type=int, default=1_000)
        parser.add_argument("--all", action="store_true", default=False)
    
    def handle(self, *args, **options) -> str | None:
        all = options.get("all")
        count = options.get("count")
        task_claculate_movie_rating(all=all, count=count)
        