from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Book
from .models import Library

# Class-Based View to Show Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # This is the HTML template to render
    context_object_name = 'library'  #  This is how the library will be referenced in the template

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all() # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # REQUIRED path
