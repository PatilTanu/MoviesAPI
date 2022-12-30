from django.db import models

# Create your models here.
class Movies(models.Model):
    tconst = models.CharField(max_length=150, primary_key=True, unique=True)
    titleType = models.CharField(max_length=150)
    primaryTitle = models.CharField(max_length=255)
    runtimeMinutes = models.IntegerField()
    genres = models.CharField(max_length=150)

class Rating(models.Model):
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE)
    averageReting = models.CharField(max_length=10)
    numVotes = models.IntegerField()
