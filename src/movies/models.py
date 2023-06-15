from datetime import timedelta
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils import timezone

from ratings.models import Rating

from movies import app_name

RATING_UPDATE_PERIOD_IN_DAYS = 1

class MovieQuerySet(models.QuerySet):
    def needs_updating(self):
        days_ago = timezone.now() - timedelta(days=RATING_UPDATE_PERIOD_IN_DAYS)
        return self.filter(
            Q(rating_updated__isnull=True) |
            Q(rating_updated__gte=days_ago)
        )

class MovieManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return MovieQuerySet(self.model, using=self._db)
    
    def needs_updating(self):
        return self.get_queryset().needs_updating()

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    
    overview = models.TextField()
    
    release_date =  models.DateTimeField(null=True, blank=True,
                        auto_now=False, auto_now_add=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    ratings = GenericRelation(Rating)
    
    rating_updated = models.DateTimeField(null=True, blank=True,
                        auto_now=False, auto_now_add=False)
    
    rating_avg = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    
    ratings_total = models.IntegerField(null=True, blank=True)
    
    objects = MovieManager()

    def get_absolute_url(self):
        return f"/{app_name}/{self.id}/"
    
    def __str__(self) -> str:
        if not self.release_date:
            return f"{self.title}"
        return f"{self.title} ({self.release_date.year})"
    
    def rating_avg_display(self):
        now = timezone.now()
        days_ago = now - timedelta(days=RATING_UPDATE_PERIOD_IN_DAYS)
        if not self.rating_updated:
            return self.calculate_rating()
        if self.rating_updated > days_ago:
            return self.rating_avg
        return self.calculate_rating()
    
    def calculate_ratings_count(self):
        return self.ratings.all().count()
    
    def calculate_ratings_avg(self):
        return self.ratings.all().avg()
    
    def calculate_rating(self, save=True):
        self.ratings_total = self.calculate_ratings_count()
        self.rating_avg = self.calculate_ratings_avg()
        self.rating_updated = timezone.now()
        if save:
            self.save()
        return self.rating_avg