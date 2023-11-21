from tasks.tasks_utils import create_update ,create_pdf_img , delete_extra_image
from celery import shared_task
from datetime import datetime
time_date = datetime.now()
@shared_task
def bookreader_api_call_task(path):
    check_task_execution(bookreader_api_call_task)
    create_pdf_img(path=path)

@shared_task
def scheduled_create_update_image():
    check_task_execution(scheduled_create_update_image)
    create_update()

@shared_task
def scheduled_delete_pdf_img():
    check_task_execution(scheduled_delete_pdf_img)
    delete_extra_image()

def check_task_execution(name_of_task):
    with open("test_hesam.txt","w") as writer:
        writer.write(f"it executed write {name_of_task} in {time_date}")


