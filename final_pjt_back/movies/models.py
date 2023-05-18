from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.ImageField(blank=True)    
    character = models.CharField(max_length=100, blank=True)

class Director(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.ImageField(blank=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)
    runtime = models.IntegerField()

    # many to many fields => 머 여러개 있으니까,,
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

class MovieActors(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)


class MovieDirectors(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.FloatField()

