# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('books/', list_books, name='book-list'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # Class-based view
]


urlpatterns += [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
