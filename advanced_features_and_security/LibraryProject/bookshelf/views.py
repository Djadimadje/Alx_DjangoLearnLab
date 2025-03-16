from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from bookshelf.models import Article

@permission_required("bookshelf.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "books/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def create_article(request):
    if request.method == "POST":
        # Form processing logic
        pass
    return render(request, "books/create_books.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    if request.method == "POST":
        # Edit logic
        pass
    return render(request, "books/edit_books.html", {"books": books})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_books(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    books.delete()
    return redirect("books_list")

