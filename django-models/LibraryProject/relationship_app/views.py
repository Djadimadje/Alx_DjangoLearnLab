from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Correctly import both Book and Library models

# Function-based view to list all books
def list_books(request):
    """
    Lists all books stored in the database with their authors.
    """
    books = Book.objects.select_related('author').all()  # Efficiently fetch related authors
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books available in that library.
    """
    model = Library  # The model associated with this view
    template_name = 'relationship_app/library_detail.html'  # Updated template path
    context_object_name = 'library'  # Context variable name in the template

    def get_context_data(self, **kwargs):
        """
        Adds additional context data if needed.
        """
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add the books related to the library
        return context

