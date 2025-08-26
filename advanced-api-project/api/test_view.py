from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create authors
        self.author1 = Author.objects.create(name="Paulo Coelho")
        self.author2 = Author.objects.create(name="George Orwell")

        # Create books with proper Author instances
        self.book1 = Book.objects.create(title="The Alchemist", author=self.author1, publication_year=1993)
        self.book2 = Book.objects.create(title="1984", author=self.author2, publication_year=1949)

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})


    # --- CRUD Tests ---
def test_create_book(self):
    data = {
        "title": "New Book",
        "author": self.author1.id,   # ✅ Pass ID, not name
        "publication_year": 2024
    }
    response = self.client.post(self.list_url, data, format="json")
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)
        

    def test_get_books_list(self):
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        data = {"title": "Updated Title", "author": "Paulo Coelho", "publication_year": 1993}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Filtering, Searching, Ordering ---
def test_filter_books_by_author(self):
    response = self.client.get(self.list_url + "?author__name=Paulo Coelho")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]["author"], self.author1.id)
    
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    # --- Permissions ---
    def test_requires_authentication_for_create(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "Anonymous", "publication_year": 2025}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
