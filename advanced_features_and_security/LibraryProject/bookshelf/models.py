from django.db import models
from django.conf import settings  # To reference the CustomUser model

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Optional ISBN field
    genre = models.CharField(max_length=50, null=True, blank=True)  # Genre field
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)  # Optional cover image
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books")  # Link to CustomUser

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

