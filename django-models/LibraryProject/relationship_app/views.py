from django.shortcuts import render

# Create your views here.
# relationship_app/views.py

# relationship_app/views.py

from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
