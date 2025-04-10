from rest_framework import serializers

from book_api.models import Genre, Book

from author_api.serializers import AuthorSerializer


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'is_deleted': {'read_only': True},
            'added_date_time': {'read_only': True},
            'updated_date_time': {'read_only': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation['genre']:
            representation['genre'] = GenreSerializer(
                instance.genre).data

        if representation['authors']:
            representation['authors'] = AuthorSerializer(
                instance.authors.all(), many=True).data

        return representation
