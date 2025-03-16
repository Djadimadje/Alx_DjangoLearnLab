from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Set up test client and initial data
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create an author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter 1", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter 2", publication_year=1998, author=self.author)

    # Test CRUD Operations
    def test_list_books(self):
        """Test retrieving all books (unauthenticated, read-only)"""
        url = reverse('book-list')  # /api/books/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    def test_retrieve_book(self):
        """Test retrieving a single book by ID (unauthenticated)"""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})  # /api/books/1/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter 1")

    def test_create_book_authenticated(self):
        """Test creating a book (authenticated user)"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')  # /api/books/create/
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], "New Book")

    def test_create_book_unauthenticated(self):
        """Test creating a book (unauthenticated should fail)"""
        url = reverse('book-create')
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book (authenticated user)"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book1.pk})  # /api/books/1/update/
        data = {"title": "Updated Book", "publication_year": 1997, "author": self.author.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        """Test updating a book (unauthenticated should fail)"""
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {"title": "Updated Book", "publication_year": 1997, "author": self.author.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Test deleting a book (authenticated user)"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})  # /api/books/1/delete/
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Test deleting a book (unauthenticated should fail)"""
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test Filtering, Searching, Ordering
    def test_filter_by_title(self):
        """Test filtering books by title"""
        url = reverse('book-list') + '?title=Harry Potter 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter 1")

    def test_search_by_title(self):
        """Test searching books by title"""
        url = reverse('book-list') + '?search=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_by_publication_year(self):
        """Test ordering books by publication_year"""
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # Oldest first
