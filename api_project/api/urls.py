from django.urls import path, include
from .views import BookList
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')