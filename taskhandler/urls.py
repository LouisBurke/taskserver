from django.conf.urls import url

from . import views

urlpatterns = [url(r'^', views.task_handler, name='task-handler')]
