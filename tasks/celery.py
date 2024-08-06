import os
from celery import Celery
from archiveAPI.settings import CELERY_BROKER_URL, INSTALLED_APPS, SCHEDULE_CREATE_UPDATE_IMAGE, SCHEDULE_DELETE_IMAGE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archiveAPI.settings')

app = Celery('archiveAPI',broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(INSTALLED_APPS)


app.conf.beat_schedule = {
    "task_create_update_image": {
        "task": "tasks.tasks.scheduled_create_update_image",
        "schedule": SCHEDULE_CREATE_UPDATE_IMAGE
    },
    "task_delete_image": {
        "task": "tasks.tasks.scheduled_delete_pdf_img",
        "schedule": SCHEDULE_DELETE_IMAGE
    }
}

