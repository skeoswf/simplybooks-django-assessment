from django.db import models


class Author(models.Model):
    email = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    image = models.CharField(max_length=25)
    favorite = models.BooleanField()
