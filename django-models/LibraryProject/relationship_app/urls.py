# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book-list'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # Class-based view
]

