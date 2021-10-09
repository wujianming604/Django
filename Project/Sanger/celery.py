#!/usr/bin/env python
#coding=utf-8

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')  #配置Django环境

app = Celery('Project')

app.config_from_object('django.conf:settings', namespace='CELERY') #

app.autodiscover_tasks()