from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "relationship_app"  # Namespace for URL resolution

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library details
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Custom authentication views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # User registration view
    path('register/', views.register, name='register'),

    # Role-based dashboard views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Book management views with permissions enforced
    path('book/add/', views.add_book, name='add_book'),  # Add a book
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),  # Edit a book
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),  # Delete a book
]

