from django.contrib import admin

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ["calculate_ratings_count",]
    readonly_fields = [ "rating_avg_display" ]
    
admin.site.register(Movie, MovieAdmin)