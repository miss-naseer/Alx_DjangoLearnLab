# query_samples.py

import os
import django

# Setup Django environment (so we can access models directly)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 🔍 1. Query all books by a specific author
print("\n📘 Books by John Doe:")
try:
    author = Author.objects.get(name="John Doe")
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author not found!")

# 🏛️ 2. List all books in a specific library
print("\n🏫 Books in Central Library:")
try:
    library = Library.objects.get(name="Central Library")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library not found!")

# 👩‍💼 3. Retrieve the librarian for a specific library
print("\n🧑‍🏫 Librarian of Central Library:")
try:
    library = Library.objects.get(name="Central Library")
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("Library or Librarian not found!")
