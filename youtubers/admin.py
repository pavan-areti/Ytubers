from django.contrib import admin
from .models import youtuber
# Register your models here.

class youtuberadmin(admin.ModelAdmin):
    list_display=['id','name','camera_type','isfeatured']
    list_editable=['isfeatured',]
    list_display_links=['name']
    list_filter=['name','camera_type','isfeatured','city']
    search_fields=['name','camera_type','city']
admin.site.register(youtuber,youtuberadmin)
