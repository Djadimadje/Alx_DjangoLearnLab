from django.urls import path
from . import views
from .views import list_books

app_name = "relationship_app"  # Recommended for namespacing

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library details
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

     # Custom login view using a custom template
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Custom logout view using a custom template
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Registration view (custom view for user registration)
    path('register/', views.register, name='register'),
    

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),  # Add a book
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),  # Edit a book
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),  # Delete a book
]

