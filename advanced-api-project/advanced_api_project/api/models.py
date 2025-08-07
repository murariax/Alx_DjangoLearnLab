from django.db import models

# Create your models here.

# The Author model stores basic information about authors.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


# The Book model stores book-related data and links each book to an author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.PositiveIntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # The ForeignKey establishes a one-to-many relationship between Author and Books.

    def __str__(self):
        return self.title
