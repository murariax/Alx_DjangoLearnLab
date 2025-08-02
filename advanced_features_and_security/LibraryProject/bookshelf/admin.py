from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list
    list_filter = ('publication_year', 'author')            # Filters on the side
    search_fields = ('title', 'author')                     # Search box fields
