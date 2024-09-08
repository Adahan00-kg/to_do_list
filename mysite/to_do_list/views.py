
from rest_framework import viewsets, permissions

from .serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import BookFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]