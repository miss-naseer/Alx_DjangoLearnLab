# bookshelf/forms.py
from django import forms
from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm  # Import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle the valid form data here
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
