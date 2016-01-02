# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.TextField(default='')),
                ('task_start_time', models.DateTimeField(verbose_name='Start Time')),
                ('task_finish_time', models.DateTimeField(default='Finish Time')),
                ('task_file_location', models.TextField(default='')),
            ],
        ),
    ]