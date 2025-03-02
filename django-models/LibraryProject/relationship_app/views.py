from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    """
    Lists all books stored in the database with their authors.
    """
    books = Book.objects.all()  # Fix: Use Book.objects.all() as required by the checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, including all books available in that library.
    """
    model = Library  
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'  

    def get_context_data(self, **kwargs):
        """
        Adds additional context data if needed.
        """
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Ensures books are passed explicitly
        return context

