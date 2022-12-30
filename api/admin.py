from django.contrib import admin

# Register your models here.
from . models import Movies, Rating

admin.site.register(Movies)
admin.site.register(Rating)
