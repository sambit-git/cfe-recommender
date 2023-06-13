from celery import shared_task

from .models import Movie

@shared_task(name="task_claculate_movie_rating")
def task_claculate_movie_rating(all=False, count=None):
    '''
    task_claculate_movie_rating(all=False, count=None)
    # celery tasks
        task_claculate_movie_rating.delay(all=False, count=None)
        task_claculate_movie_rating.apply_async(
            kwargs = { "all": False, "count": 12}, countdown=30)
    '''
    if all:
        qs = Movie.objects.all()
    else:
        qs = Movie.objects.needs_updating()
    
    qs.order_by("rating_updated")
    if isinstance(count, int):
        qs = qs[:count]
    
    for obj in qs:
        obj.calculate_rating(save=True)