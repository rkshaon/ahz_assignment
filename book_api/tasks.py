from celery import shared_task

from django.utils import timezone

from book_api.models import Book


@shared_task
def archive_books_checker():
    print("Archive books checker task executed.", timezone.now())
    # Get all books that are older than 30 days
    books_to_archive = Book.objects.filter(
        is_archived=False,
        created_at__lt=timezone.now() - timezone.timedelta(days=30)
    )
    # Archive them
    for book in books_to_archive:
        book.is_archived = True
        book.save()
    return
