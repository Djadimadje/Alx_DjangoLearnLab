from django.urls import path
from django.http import JsonResponse
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# Fallback views to handle requests without a `pk`
def missing_pk_response(request):
    return JsonResponse({"error": "Book ID is required."}, status=400)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),            # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a book
    path('books/create/', BookCreateView.as_view(), name='book-create'), # Create a book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book


    # Handle missing `pk` for update and delete
    path('books/update/', missing_pk_response, name='book-update-missing'),
    path('books/delete/', missing_pk_response, name='book-delete-missing'),

]
