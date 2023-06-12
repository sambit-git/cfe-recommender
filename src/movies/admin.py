from django.contrib import admin

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "ratings_total", "rating_avg"]
    readonly_fields = [ "rating_avg_display" ]
    
admin.site.register(Movie, MovieAdmin)