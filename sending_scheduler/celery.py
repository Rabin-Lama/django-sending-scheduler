from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sending_scheduler.settings')

app = Celery('sending_scheduler')

app.config_from_object(settings, namespace='CELERY')

# # Load task modules from all registered Django apps.
app.autodiscover_tasks()
