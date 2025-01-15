from django.db import models
from .author import Author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    image = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    sale = models.BooleanField()
    description = models.CharField(max_length=25)
