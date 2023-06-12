from datetime import timedelta
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone

from ratings.models import Rating

RATING_UPDATE_PERIOD = 1

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
    
    def rating_avg_display(self):
        now = timezone.now()
        if not self.rating_updated:
            return self.calculate_rating()
        if self.rating_updated > now - timedelta(minutes=RATING_UPDATE_PERIOD):
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