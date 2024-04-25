import xadmin
# from django.contrib import admin
from .models import SangerSamples, SangerZipFiles


class SangerZipFilesAdmin(object):
    #查询结果字段
    list_display = ('id', 'fileName', 'sampleNumbers', 'status', 'analysisStatus', 'createdTime')
    #搜索框
    search_fields = ['fileName', 'sampleNumbers', 'status', 'analysisStatus']
    #过滤框
    list_filter = ['fileName', 'sampleNumbers', 'status', 'analysisStatus']
    # list_exclude = ['updateTime']
    # 每页显示的数据行数
    list_per_page = 20
    show_bookmarks = False
    fields = ('fileName', 'sampleNumbers', )

    # def get_queryset(self, request):
    #     qs = super(SangerZipFilesAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)


class SangerSamplesAdmin(object):
    list_display = ('id', 'sampleName', 'chrom', 'pos', 'genoType', 'abiPngUrl', 'created_time', 'update_time')
    search_fields = ['sampleName', 'chrom', 'abiPngUrl']
    list_filter = ['sampleName', 'chrom']
    list_per_page = 20
    show_bookmarks = False
    #隐藏字段
    # list_exclude = ['abiFileUrl', 'created_time']
    #只读字段
    readonly_fields = ['sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl']

    fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)


xadmin.site.register(SangerZipFiles, SangerZipFilesAdmin)
xadmin.site.register(SangerSamples, SangerSamplesAdmin)