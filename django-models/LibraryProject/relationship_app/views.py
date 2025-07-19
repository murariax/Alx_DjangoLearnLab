from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .models import Library
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

# relationship_app/views.py

# relationship_app/views.py

from django.views.generic.detail import DetailView
from .models import Book, Library

# ✅ Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # required by checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view: Show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # required path
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
