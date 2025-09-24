
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
# This is the book Serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Book
        fields = "__all__"

# This is the author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "name"

# This is the Nested Book Serializer
class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source=Author.name, read_only = True)
    class Meta:
        model = Book
        fields =["title", "author", "publication_year", "name"]
    # This is Validation method that validate if the attribute "publictaion_year" of the model is not in the future.
    def validate(self, data):
        now = datetime.now()
        if data["publication_year"] > now:
            raise serializers.ValidationError("The publication year cannot be in the future")