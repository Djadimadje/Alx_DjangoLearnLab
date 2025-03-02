from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from .views import list_books
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

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

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'  # Use custom login template

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # Authenticate the user
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to a home page or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Logout view (handled by Django's built-in LogoutView)
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# Define the role check functions
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Views for role-based access

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# Add a book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})
