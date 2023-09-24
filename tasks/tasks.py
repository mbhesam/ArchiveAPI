from tasks.tasks_utils import create_update ,create_pdf_img
from celery import shared_task

@shared_task
def bookreader_run_task():
    check_task_execution()
    create_pdf_img()

@shared_task
def scheduled_task_run():
    check_task_execution()
    create_update()

def check_task_execution():
    with open("test_hesam.txt","w") as writer:
        writer.write("it executed write")


