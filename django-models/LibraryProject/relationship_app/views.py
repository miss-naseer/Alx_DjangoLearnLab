from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').all()  # fetch all books with their author
    return render(request, 'list_books.html', {'books': books})


from django.views.generic import DetailView
from .models import Library

# Class-Based View to Show Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # This is the HTML template to render
    context_object_name = 'library'  #  This is how the library will be referenced in the template

