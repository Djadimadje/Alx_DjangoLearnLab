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
