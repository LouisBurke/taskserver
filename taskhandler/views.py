from uuid import uuid4

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Tasks
from .tasks import task_func

# Create your views here.
@csrf_exempt
def task_handler(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        task_id = uuid4()
        task_file_name = str(task_id) + '.log'

        task_func(data, task_file_name, task_id)

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
