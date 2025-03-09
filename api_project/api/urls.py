from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet
from django.urls import include

# Create router instance
router = DefaultRouter()
# Register BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]
