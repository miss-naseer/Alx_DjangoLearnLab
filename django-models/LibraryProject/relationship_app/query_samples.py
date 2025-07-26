# query_samples.py
import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# === 1. Query all books by a specific author ===
print("\n📘 Books by John Doe:")
try:
    author = Author.objects.get(name="John Doe")
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("❌ Author not found!")

# === 2. List all books in a specific library ===
library_name = "Central Library"
print(f"\n🏫 Books in {library_name}:")
try:
    library = Library.objects.get(name=library_name)  # ✅ Now contains the required line
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("❌ Library not found!")

# === 3. Retrieve the librarian for a library ===
print(f"\n🧑‍🏫 Librarian of {library_name}:")
try:
    library = Library.objects.get(name=library_name)  # ✅ Using the same variable here
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("❌ Library or Librarian not found!")
