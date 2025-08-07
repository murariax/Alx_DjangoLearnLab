from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    # Custom validation: publication year should not be in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include author name and nested books

    # Note: 'books' uses the related_name from the Book model's ForeignKey.
