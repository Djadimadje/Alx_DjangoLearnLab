from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    """
    Lists all books stored in the database with their authors.
    """
    books = Book.objects.select_related('author').all()  # Efficiently fetch related authors
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books available in that library.
    """
    model = Library  # The model associated with this view
    template_name = 'library_detail.html'  # Template to render
    context_object_name = 'library'  # Context variable name in the template

    def get_context_data(self, **kwargs):
        """
        Adds additional context data if needed.
        """
        context = super().get_context_data(**kwargs)
        # You can add extra context here if required
        return context
