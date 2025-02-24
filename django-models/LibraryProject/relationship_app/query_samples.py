from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author '{author_name}' does not exist."

# List all books in a library
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian.name if librarian else "No librarian assigned."
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

# Example Usage
if __name__ == "__main__":
    print("Books by Author:")
    print(query_books_by_author("J.K. Rowling"))

    print("\nBooks in Library:")
    print(query_books_in_library("Central Library"))

    print("\nLibrarian for Library:")
    print(query_librarian_for_library("Central Library"))
