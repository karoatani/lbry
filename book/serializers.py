from rest_framework.serializers import ModelSerializer
from .models import Book,Category
from author.serializers import AuthorSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ["id","name","image","author","category","description"]
