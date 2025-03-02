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
]

