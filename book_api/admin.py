from django.contrib import admin

from book_api.models import Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_code',
        'title',
        'published_date',
        'is_archived',
        'added_date_time',
        'updated_date_time'
    )
    search_fields = ('title',)
    list_filter = ('genre',)
    ordering = ('-added_date_time',)
    list_per_page = 10


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'slug',
        'added_date_time',
        'updated_date_time'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('-added_date_time',)
    list_per_page = 10
