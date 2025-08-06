from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Author(models.Model):
    """Represents a book author"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Represents a book and its relation to an author"""
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

