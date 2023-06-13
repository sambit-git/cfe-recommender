from .models import Movie

def task_claculate_movie_rating(all=False, count=None):
    if all:
        qs = Movie.objects.all()
    else:
        qs = Movie.objects.needs_updating()
    
    qs.order_by("rating_updated")
    if isinstance(count, int):
        qs = qs[:count]
    
    for obj in qs:
        obj.calculate_rating(save=True)