from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Tag, Comment
from taggit.forms import TagWidget  # Import TagWidget from taggit.forms
from django.forms import widgets  # Explicitly import widgets

# User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]

# Post Creation and Update Form with Tagging
class PostForm(forms.ModelForm):
    # Replace the old tags field widget with TagWidget
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget to handle tag input
        required=False  # Tags are optional
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {  # Ensure "widgets" is explicitly present
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'content': widgets.Textarea(attrs={'class': 'form-control'}),
        }

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {  # Ensure "widgets" is explicitly present
            'content': widgets.Textarea(attrs={'class': 'form-control'}),
        }
