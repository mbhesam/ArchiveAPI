import os
from celery import Celery
from celery.schedules import crontab
from archiveAPI.settings import CELERY_BROKER_URL, INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archiveAPI.settings')

app = Celery('archiveAPI',broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(INSTALLED_APPS)


