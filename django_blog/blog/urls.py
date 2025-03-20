from django.urls import path
from .views import (
    login_view, logout_view, register_view, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, search_view,
    add_comment, edit_comment, delete_comment
)
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
    # Authentication URLs
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),

    # Blog Post URLs (CRUD)
    path("", PostListView.as_view(), name="post-list"),  # Homepage displaying all posts
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View a single post
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Create a new post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Edit a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete a post

    # Comment URLs (Create, Edit, Delete)
    path("post/<int:post_id>/comments/new/", add_comment, name="add-comment"),  # Add new comment
    path("comment/<int:pk>/update/", edit_comment, name="edit-comment"),  # Edit comment
    path("comment/<int:pk>/delete/", delete_comment, name="delete-comment"),  # Delete comment

    # Password Reset URLs (Optional)
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="blog/password_reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="blog/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="blog/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="blog/password_reset_complete.html"), name="password_reset_complete"),

    # Search URL
    path("search/", search_view, name="search"),

    # URL for viewing posts by tag
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
]
