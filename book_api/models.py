from django.db import models
from django.db.models.functions import Lower

from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.text import slugify

import uuid


def generate_book_code():
    """
        Generates a unique book code.
    """
    current_time = now().strftime('%Y%m%d%H%M%S%f')
    book_code = str(uuid.uuid4().int)[:10]
    book_code = int(f'{book_code}{current_time}')

    return book_code


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='Unique Genre name is not case sensitive.'
            )
        ]

    def clean(self):
        if Genre.objects.filter(
            name__iexact=self.name
        ).exclude(pk=self.pk).exists():
            raise ValidationError(
                "A genre with this name (case-insensitive) already exists.")

    def save(self, *args, **kwargs):
        self.clean()

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    book_code = models.CharField(
        max_length=255,
        default=generate_book_code,
        unique=True,
        editable=False
    )
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(
        'book_api.Genre',
        on_delete=models.CASCADE,
        related_name='books',
        blank=True,
        null=True
    )
    authors = models.ManyToManyField(
        'author_api.Author',
        blank=True,
        related_name='books')
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(
        blank=True,
        null=True
    )
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
