import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinegalaxy.settings')

app = Celery("cinegalaxy")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-movie-rating-every-30": {
        'task': 'task_claculate_movie_rating',
        'schedule': 60 * 30, # every 30 minutes
        'kwargs': { "count": 20_000 }
    }
}