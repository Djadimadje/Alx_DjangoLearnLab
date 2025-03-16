from django.db import models

class Author(models.Model):

  """
    Author model to represent an author in the system.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):

   """
    Book model to represent a book.
    The Book is linked to an Author through a ForeignKey relationship.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

