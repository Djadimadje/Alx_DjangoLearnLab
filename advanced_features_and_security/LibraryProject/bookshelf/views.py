from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from myapp.models import Article

@permission_required("myapp.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/article_list.html", {"articles": articles})

@permission_required("myapp.can_create", raise_exception=True)
def create_article(request):
    if request.method == "POST":
        # Form processing logic
        pass
    return render(request, "articles/create_article.html")

@permission_required("myapp.can_edit", raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        # Edit logic
        pass
    return render(request, "articles/edit_article.html", {"article": article})

@permission_required("myapp.can_delete", raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("article_list")

