from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

# Create router instance
router = DefaultRouter()
# Register BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
    path('get_token/', obtain_auth_token, name='get_token'),
]
