#!/usr/bin/env python
#coding=utf-8


# import pymysql
# pymysql.install_as_MySQLdb()
# from __future__ import absolute_import, unicode_literals
# from .celery import app as celery_app
# __all__ = ['celery_app']
from celery import Celery
app = Celery('project')                                # 创建 Celery 实例
app.config_from_object('Project.config')               # 加载配置模块