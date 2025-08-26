from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
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


# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can read


# Retrieve details of a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users can create


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list all books or create a new one.
    - GET /api/books/ → returns list of all books
    - POST /api/books/ → creates a new book (authenticated only)
    """


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    """
BookListView with filtering, searching, and ordering.

Examples:
- Filter by author: /api/books/?author=John
- Search by title/author: /api/books/?search=Python
- Order by year (desc): /api/books/?ordering=-publication_year
"""

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] 