# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views



urlpatterns = [
    path('books/', list_books, name='book-list'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # Class-based view
    path('register/', views.register, name='register'),  # ✅ function-based for register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ class-based
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', views.admin_view, name='admin-view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-view'),
    path('member-dashboard/', views.member_view, name='member-view'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

]

