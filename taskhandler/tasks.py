import subprocess

from json import loads
from time import time

from celery import shared_task

from .models import Tasks

@shared_task
def task_func(params_json, task_file_name, task_id):
    params_dict = loads(params_json)

    cmd = [params_dict['command']]
    args = params_dict['arguments']

    task = cmd + args

    task_object = Tasks()
    task_object.task_id = task_id
    task_object.task_start_time = str(time())
    task_object.task_file_location = task_file_name
    task_object.save()

    with open(task_file_name, 'a') as logfile:
        p = subprocess.call(
            task,
            stdout=logfile,
            stderr=subprocess.STDOUT
        )

    task_object.task_finish_time = str(time())
    task_object.save()
