from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model

from movies.models import Movie
from ratings.models import Rating

from ratings.task import generate_fake_reviews

User = get_user_model()

class Command(BaseCommand):
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--users", default=1000, type=int)
        parser.add_argument("--show-total", action="store_true", default=False)
    
    def handle(self, *args, **options) -> str | None:
        count = options.get("count")
        show_total = options.get("show_total")
        user_count = options.get("users")
        new_ratings = generate_fake_reviews(count = count, users=user_count)
        print(f"New ratings: {len(new_ratings)}")
        if show_total:
            qs = Rating.objects.all()
            print(f"Total ratings: {qs.count()}")
        