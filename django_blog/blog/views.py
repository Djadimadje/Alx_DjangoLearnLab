from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegisterForm, ProfileUpdateForm, CommentForm
from .models import Profile, Post, Comment

# User Registration View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create a profile for the new user
            login(request, user)  # Automatically log in the user
            messages.success(request, "Registration successful. Welcome!")
            return redirect("blog:profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("blog:profile")  # Redirect to profile page after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# User Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("blog:login")  # Redirect to login page after logout

# User Profile View
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("blog:profile")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, "blog/profile.html", {"form": form, "profile": profile})

# ============================
# CRUD Operations for Blog Posts
# ============================

# ListView: Displays all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template should be in /templates/blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show newest posts first

# DetailView: Displays a single blog post with comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template should be in /templates/blog/post_detail.html
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()  # Fetch all comments for this post
        context['comments'] = comments
        context['comment_form'] = CommentForm()  # Provide a form to add new comments
        return context

# CreateView: Allows authenticated users to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template for creating a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# UpdateView: Allows the author of a post to edit it
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # Reuse the same template as CreateView
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the post's author can edit

# DeleteView: Allows the author of a post to delete it
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Confirmation template
    success_url = reverse_lazy('post-list')  # Redirect to the post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete

# ============================
# CRUD Operations for Comments
# ============================

# CreateView: Allows authenticated users to create a comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('blog:post-detail', pk=post.id)
    else:
        form = CommentForm()
    return redirect('blog:post-detail', pk=post.id)

# UpdateView: Allows the comment author to edit their comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('blog:post-detail', pk=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been updated.")
            return redirect('blog:post-detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'blog/comment_form.html', {'form': form})

# DeleteView: Allows the comment author to delete their comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You do not have permission to delete this comment.")
    else:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    return redirect('blog:post-detail', pk=comment.post.id)

