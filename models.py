from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title
