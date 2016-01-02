import django_rq
import subprocess

from json import loads
from time import time
from uuid import uuid4

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Tasks

def task_func(params_json, task_file_name, task_id):
    params_dict = loads(params_json)

    cmd = [params_dict['command']]
    args = params_dict['arguments']

    task = cmd + args

    task_object = Tasks()
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

# Create your views here.
@csrf_exempt
def task_handler(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        task_id = uuid4()
        task_file_name = str(task_id) + '.log'

        django_rq.enqueue(
            task_func,
            params_json=data,
            task_file_name=task_file_name,
            task_id=task_id
        )

        message = str(task_id)
        status = 200
    elif request.method == 'GET':
        tasks = Tasks.objects.all()
        task_list = list()
        for task in tasks:
            task_dict = dict()
            task_dict['task_id'] = task.task_id
            task_dict['task_start_time'] = task.task_start_time
        message = 'JSON Blob'
        status = 200

    return HttpResponse(message, status=status)


def task_details(request):
    return HttpResponse("Hello, world. You're at the polls index.")
