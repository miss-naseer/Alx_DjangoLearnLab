# bookshelf/forms.py
from django import forms
from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
