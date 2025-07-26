from django.shortcuts import render

# Create your views here.
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').all()  # fetch all books with their author
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
