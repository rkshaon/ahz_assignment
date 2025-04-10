from django.contrib import admin

from author_api.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_birth',
        'is_deleted',
        'added_date_time',
        'updated_date_time'
    )
    search_fields = ('name',)
    list_filter = ('is_deleted',)
    ordering = ('-added_date_time',)
    date_hierarchy = 'added_date_time'
    list_per_page = 10
    readonly_fields = ('added_date_time', 'updated_date_time')
