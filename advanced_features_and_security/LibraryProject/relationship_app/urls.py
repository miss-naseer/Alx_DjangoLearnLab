from django.urls import path
from .views import list_books, LibraryDetailView, add_book

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('add/', add_book, name='add_book'),
]
