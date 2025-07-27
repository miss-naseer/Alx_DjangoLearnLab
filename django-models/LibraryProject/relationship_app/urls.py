from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from .views import list_books
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # connect relationship_app urls
]

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),          #  Add Book URL
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  #  Edit Book URL
]
