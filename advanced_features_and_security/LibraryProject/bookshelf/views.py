from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from bookshelf.models import Book, Article
from .forms import ExampleForm, BookForm  # ✅ Added missing import

@permission_required("bookshelf.can_view", raise_exception=True)
def article_list(request):
    books = Book.objects.all()  # ✅ Fixed incorrect model reference
    return render(request, "books/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def create_article(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)  # ✅ ExampleForm now used
        if form.is_valid():
            # Form processing logic (modify as needed)
            pass
    else:
        form = ExampleForm()
    
    return render(request, "books/create_books.html", {"form": form})

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_books(request, books_id):
    book = get_object_or_404(Book, id=books_id)  # ✅ Fixed model reference
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books_list")
    else:
        form = BookForm(instance=book)
    
    return render(request, "books/edit_books.html", {"form": form})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_books(request, books_id):
    book = get_object_or_404(Book, id=books_id)  # ✅ Fixed model reference
    book.delete()
    return redirect("books_list")

