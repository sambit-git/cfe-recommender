from django.contrib import admin

# Register your models here.
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = [ "user"]
    list_display = [ "content_type", "content_object", "value" ]
    readonly_fields = ["content_object"]

admin.site.register(Rating, RatingAdmin)