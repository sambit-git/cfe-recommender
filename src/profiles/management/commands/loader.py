from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from cinegalaxy import utils as cinegalaxy_utils

from movies.models import Movie

User = get_user_model()

class Command(BaseCommand):
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--movies", action="store_true", default=False)
        parser.add_argument("--users", action="store_true", default=False)
        parser.add_argument("--show-total", action="store_true", default=False)
    
    def handle(self, *args, **options) -> str | None:
        count = options.get("count")
        show_total = options.get("show_total")
        load_movies = options.get("movies")
        generate_users = options.get("users")
        
        if load_movies:
            movie_dataset = cinegalaxy_utils.load_movie_data(limit=count)
            movies_new = [Movie(**mov) for mov in movie_dataset]
            movie_bulk = Movie.objects.bulk_create(movies_new,
                            ignore_conflicts=True)
            print(f"New movies: {len(movie_bulk)}")
            
            if show_total:
                print(f"Total movies: {Movie.objects.count()}")
        elif generate_users:
            profiles = cinegalaxy_utils.get_fake_profiles(count=count)
            
            new_users = []
            for profile in profiles:
                new_users.append( User(**profile) )
            
            user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
            print(f"New users: {len(user_bulk)}")
            
            if show_total:
                print(f"Total users: {User.objects.count()}")