from django.contrib import admin
from .models import Book

# Custom admin class to control display
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list
    list_filter = ('publication_year', 'author')            # Filter sidebar
    search_fields = ('title', 'author')                     # Search bar functionality

# Register model with the custom admin class
admin.site.register(Book, BookAdmin)


# Register your models here.
