#!coding=utf-8
#给上传的文件重命名

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from Project import settings

class FileStorage(FileSystemStorage):

    def __init__(self, location=settings.uploadSanger_DIR, base_url=settings.uploadSangerUrl):
        super(FileStorage, self).__init__(location, base_url)

    #重写_save方法
    def _save(self, name, content):
        # name为上传文件名称
        import os, time, random, re
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        samplename = re.split(r'[\\/]',os.path.splitext(name)[0])[-1]
        # 文件目录(uploadSanger)
        # d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%M%S')
        # 重写合成文件名
        newName = samplename + "_" + fn + ext
        # name = os.path.join(name+'_', fn + ext)
        # 调用父类方法
        return super(FileStorage, self)._save(newName, content)