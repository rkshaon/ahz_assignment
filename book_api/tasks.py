from celery import shared_task

from django.utils import timezone

from book_api.models import Book


@shared_task
def archive_books_checker():
    Book.objects.filter(
        is_archived=False,
        published_date__lt=timezone.now() - timezone.timedelta(days=365*10)
    ).update(
        is_archived=True
    )

    return
