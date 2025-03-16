from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Import for permission control
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books, open to all users with optional filtering
class BookListView(generics.ListAPIView):


    serializer_class = BookSerializer  # Serialize Book instances

    def get_queryset(self):
        # Custom behavior: Filter books by year if provided in query params
        queryset = Book.objects.all()
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(publication_year__gte=year)
        return queryset

# DetailView: Retrieve a single book by ID, open to all users
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by its ID. Accessible to all users (read-only).
    """
    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Serialize the book data

# CreateView: Add a new book, restricted to authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book instance. Only authenticated users can access this endpoint.
    Custom behavior: Logs the creation event for debugging or auditing.
    """
    queryset = Book.objects.all()  # Required by generic view
    serializer_class = BookSerializer  # Handle creation with serializer
    permission_classes = [IsAuthenticated]  # Restrict to logged-in users

    def perform_create(self, serializer):
        # Custom behavior: Add logging or preprocessing before saving
        instance = serializer.save()
        print(f"Book created: {instance.title} by {self.request.user}")

# UpdateView: Modify an existing book, restricted to authenticated users
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID. Only authenticated users can modify books.
    Custom behavior: Ensures title is not empty before saving.
    """
    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Handle updates with serializer
    permission_classes = [IsAuthenticated]  # Restrict to logged-in users

    def perform_update(self, serializer):
        # Custom validation: Prevent empty titles
        if not self.request.data.get('title'):
            raise serializer.ValidationError("Title cannot be empty.")
        instance = serializer.save()
        print(f"Book updated: {instance.title} by {self.request.user}")

# DeleteView: Remove a book, restricted to authenticated users
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID. Only authenticated users can perform this action.
    No additional customization beyond permission enforcement.
    """
    queryset = Book.objects.all()  # Queryset for all books
    serializer_class = BookSerializer  # Required, though not used for deletion
    permission_classes = [IsAuthenticated]  # Restrict to logged-in users
