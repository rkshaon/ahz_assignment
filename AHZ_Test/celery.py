from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
# from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AHZ_Test.settings')
app = Celery('AHZ_Test')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'run-every-1-minutes': {
        'task': 'book_api.tasks.archive_books_checker',
        'schedule': 60,
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
