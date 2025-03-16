from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  # ✅ Correct imports
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books, open to all users with optional filtering
class BookListView(generics.ListAPIView):
    """
    List all books. Open to all users, but can be filtered by publication year.
    """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Read-only access for unauthenticated users

    def get_queryset(self):
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
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ Read-only access for unauthenticated users


# CreateView: Add a new book, restricted to authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book entry. Only authenticated users can add books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can create books

    def perform_create(self, serializer):
        instance = serializer.save()
        print(f"Book created: {instance.title} by {self.request.user}")


# UpdateView: Modify an existing book, restricted to authenticated users
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID. Only authenticated users can modify books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can update books

    def perform_update(self, serializer):
        if not self.request.data.get('title'):
            raise serializers.ValidationError("Title cannot be empty.")
        instance = serializer.save()
        print(f"Book updated: {instance.title} by {self.request.user}")


# DeleteView: Remove a book, restricted to authenticated users
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID. Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only authenticated users can delete books

