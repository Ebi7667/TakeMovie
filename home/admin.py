from django.contrib import admin
from .models import Movies
# Register your models here.
@admin.register(Movies)
class AdminMovie(admin.ModelAdmin):
    list_display=['name','zhanr','running_time']
    list_editable=['zhanr','running_time']
