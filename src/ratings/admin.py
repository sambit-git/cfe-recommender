from django.contrib import admin

# Register your models here.
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = [ "user"]
    list_display = [ "content_type", "content_object", "object_id", "value", "user", "active"]
    readonly_fields = ["content_object", "timestamp"]

admin.site.register(Rating, RatingAdmin)