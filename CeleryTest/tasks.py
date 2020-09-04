from .celery import app
from celery import shared_task

@shared_task
def hello_world():
    print("Hello world")


