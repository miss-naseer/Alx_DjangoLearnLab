from django.db import models
from rest_framework import serializers
class Author(models.Model):
    """
    Author model represents a book writer.
    - name: stores the author's name
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents an individual book.
    - title: the book's title
    - publication_year: year of publication
    - author: foreign key linking the book to its author (one-to-many relationship)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'