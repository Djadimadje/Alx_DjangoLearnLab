from django import forms
from .models import Book, Article, CustomUser

# ExampleForm (You may need to modify this based on what it's supposed to do)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'added_by']

# Article Form
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

# Custom User Registration Form
class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'date_of_birth', 'profile_photo']

