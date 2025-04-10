from rest_framework import viewsets, permissions

from author_api.models import Author

from author_api.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
