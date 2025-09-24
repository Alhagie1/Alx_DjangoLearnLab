
from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Book
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "name"

class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source=Author.name, read_only = True)
    class Meta:
        model = Book
        fields =["title", "author", "publication_year", "name"]
    def validate(self, data):
        now = datetime.now()
        if data["publication_year"] > now:
            raise serializers.ValidationError("The publication year cannot be in the future")