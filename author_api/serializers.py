from rest_framework import serializers

from author_api.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {'required': True},
        }
