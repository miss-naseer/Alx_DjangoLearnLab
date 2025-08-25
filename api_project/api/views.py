from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.

# View to list all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()     # fetch all books
    serializer_class = BookSerializer # use our serializer
