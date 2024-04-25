from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .settings import uploadSanger_DIR
from django.views.static import serve

import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url('', xadmin.site.urls),
    # path('runscript/', views.runscript),
    url(r'^uploadSanger/(?P<path>.*)$', serve, {"document_root":uploadSanger_DIR}), #设置了这个才能够下载文件。
]
