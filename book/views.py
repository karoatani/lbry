from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .permissons import CurrentUserOrAdmin,CurrentStaffOrAdmin
from .models import Book, Category
from .serializers import BookSerializer,CategorySerializer

# Create your views here.


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]


    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [CurrentUserOrAdmin]
        
        return super(BookView,self).get_permissions()


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CurrentStaffOrAdmin]

