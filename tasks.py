import time

from celery import shared_task

from config.celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    time.sleep(5)
    return x + y

# @shared_task
# def add(x, y):
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)
