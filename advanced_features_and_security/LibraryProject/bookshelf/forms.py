# bookshelf/forms.py
from django import forms
from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
