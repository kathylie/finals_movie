from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Director(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    rating = models.PositiveBigIntegerField()
    comment = models.TextField()
    
    def __str__(self):
        return f"Review for {self.mavie.title} by {self.user_name}"