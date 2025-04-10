from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from django.core.cache import cache

from book_api.models import Genre, Book

from book_api.serializers import GenreSerializer, BookSerializer


CACHE_KEY = "books_list"


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'authors__name']

    def list(self, request, *args, **kwargs):
        cached_data = cache.get(CACHE_KEY)
        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        # cache for 15 minutes
        cache.set(CACHE_KEY, response.data, timeout=60 * 15)
        return response

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.delete(CACHE_KEY)
        return instance

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete(CACHE_KEY)
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete(CACHE_KEY)
