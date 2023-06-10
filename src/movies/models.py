from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    release_date =  models.DateTimeField(null=True, blank=True,
                        auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)