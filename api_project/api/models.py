from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)   # short text, indexed by length
    author = models.CharField(max_length=100)  # author’s name

    def __str__(self):
        return f"{self.title} by {self.author}"
