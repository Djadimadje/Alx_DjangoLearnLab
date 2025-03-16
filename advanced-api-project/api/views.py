from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  # Import permission classes
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books, open to all users with optional filtering
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books. Supports optional filtering by publication year
    via query parameter (e.g., ?year=2000). Accessible to all users (read-only).
    """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Explicitly allow read-only access

    def get_queryset(self):
        # Custom filter: Return books published on or after the specified year
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
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Explicitly allow read-only access

# CreateView: Add a new book, restricted to authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book instance. Only authenticated users can access this endpoint.
    Custom behavior: Logs the creation event.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

    def perform_create(self, serializer):
        # Custom hook: Log creation event
        instance = serializer.save()
        print(f"Book created: {instance.title} by {self.request.user}")

# UpdateView: Modify an existing book, restricted to authenticated users
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID. Only authenticated users can modify books.
    Custom behavior: Ensures title is not empty before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

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
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only
