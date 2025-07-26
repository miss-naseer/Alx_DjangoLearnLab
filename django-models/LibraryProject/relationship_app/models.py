from django.db import models

# Create your models here.
# 1. Author: One Author can write many Books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book: Each Book has one Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # One-to-Many

    def __str__(self):
        return self.title

# 3. Library: One Library can have many Books
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # Many-to-Many

    def __str__(self):
        return self.name

# 4. Librarian: One Librarian manages one Library (and vice versa)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # One-to-One

    def __str__(self):
        return self.name
