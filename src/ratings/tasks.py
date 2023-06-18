import random
from celery import shared_task

from django.db.models import Avg, Count
from django.contrib.auth import get_user_model

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from movies.models import Movie
from .models import Rating, RatingChoice

User = get_user_model()

@shared_task(name="generate_fake_reviews")
def generate_fake_reviews(count=100, users=10, null_avg=False):
    user_s = User.objects.first()
    user_e = User.objects.last()
    random_user_ids = random.sample(range(user_s.id, user_e.id), users)
    users = User.objects.filter(id__in=random_user_ids)
    movies = Movie.objects.all().order_by("?")[:count]
    if null_avg:
        movies = Movie.objects.filter(
            rating_avg__isnull=True).order_by("?")[:count]
    n_movies = movies.count()
    rating_choices = [choice for choice in RatingChoice.values if choice is not None]
    rand_ratings = [random.choice(rating_choices) for _ in range(n_movies)]
    
    new_ratings = []
    for movie in movies:
        rating_obj = Rating.objects.create(
            content_object=movie,
            value=rand_ratings.pop(),
            user=random.choice(users)
        )
        new_ratings.append(rating_obj.id)
    return new_ratings


@shared_task(name="task_update_movie_ratings")
def task_update_movie_ratings(movie_id = None):
    start = timezone.now()
    ctype = ContentType.objects.get_for_model(Movie)

    qs = Rating.objects.filter(content_type = ctype)
    if movie_id is not None:
        qs.filter(object_id = movie_id)

    agg_ratings = qs.values('object_id').annotate(
        average = Avg("value"),
        count = Count('object_id'))
    
    for agg_rate in agg_ratings:
        qs = Movie.objects.filter(id=agg_rate['object_id'])
        qs.update(
            rating_avg = agg_rate['average'],
            ratings_total = agg_rate['count'],
            rating_updated = timezone.now()
        )
    print(f"Time taken: {(timezone.now()- start).total_seconds()} seconds")