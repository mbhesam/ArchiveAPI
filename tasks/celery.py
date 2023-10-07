import os
from celery import Celery
from celery.schedules import crontab
from archiveAPI.settings import CELERY_BROKER_URL, INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archiveAPI.settings')

app = Celery('archiveAPI',broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(INSTALLED_APPS)


app.conf.beat_schedule = {
    'run-task-every-day': {
        'task': 'tasks.tasks.scheduled_task_run',
        'schedule': crontab(hour='1-23', minute='0', day_of_week='*'),
    },
    'run-task-every-day': {
        'task': 'tasks.tasks.scheduled_delete_pdf_img',
        'schedule': crontab(hour='1', minute='0', day_of_week='*'),
    },
}

