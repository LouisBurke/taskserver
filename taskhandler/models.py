from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_id = models.TextField(default='')
    task_start_time = models.TextField('')
    task_finish_time = models.TextField(default='')
    task_file_location = models.TextField(default='')
