from rest_framework.viewsets import ModelViewSet
from book.permissons import CurrentUserOrAdmin
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [CurrentUserOrAdmin]
