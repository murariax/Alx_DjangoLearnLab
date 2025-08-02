from django.urls import path, include
from .views import BookList
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/', BookList.as_view(), name='book-list'),
]
