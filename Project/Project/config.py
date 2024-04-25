#!/usr/bin/env python
#coding=utf-8

CELERY_BROKER_URL = 'redis://10.1.210.69:6379/0' # Broker配置，使用Redis作为消息中间件

CELERY_RESULT_BACKEND = 'redis://10.1.210.69:6379/0' # BACKEND配置，这里使用redis

CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案

# WSGI_APPLICATION = 'Project.wsgi.application'
CELERY_IMPORTS = (     # 指定导入的任务模块,可以指定多个
    'Sanger.tasks',
)