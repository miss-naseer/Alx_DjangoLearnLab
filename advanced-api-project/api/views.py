from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Anyone can read, only authenticated can create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve, update, or delete a specific book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Anyone can read, only authenticated can edit/delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list all books or create a new one.
    - GET /api/books/ → returns list of all books
    - POST /api/books/ → creates a new book (authenticated only)
    """
