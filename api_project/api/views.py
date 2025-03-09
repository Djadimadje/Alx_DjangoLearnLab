from rest_framework.generics import ListAPIView  # ✅ Ensure this import is present
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # ✅ Ensure it extends ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer

