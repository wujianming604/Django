from django.contrib.auth.models import User
from django.db import models
from django import forms
from .storage import FileStorage


class SangerSamples(models.Model):
    '''
    列表title：id, sampleName, chrom, pos, ref, alt, genoType, abiFileUrl, abiPngUrl, createTime, updateTime
    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sampleName = models.CharField(max_length=50, verbose_name="sampleName")
    chrom = models.CharField(max_length=5, verbose_name="chrom")
    pos = models.PositiveIntegerField( verbose_name="pos")
    # ref = models.CharField(max_length=25, verbose_name="ref")
    # alt = models.CharField(max_length=25, verbose_name="alt")
    genoType = models.CharField(max_length=25, verbose_name="genoType")
    abiFileUrl = models.CharField(max_length=255, verbose_name="abiFileUrl")
    abiPngUrl = models.ImageField(max_length=255, verbose_name="abiPngUrl" , upload_to = "uploadSanger/",storage=FileStorage())
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="createdTime")
    update_time = models.DateTimeField(auto_now=True, verbose_name="updateTime")

    class Meta:
        verbose_name = verbose_name_plural = 'Sanger结果'
    
    def __str__(self):
        return self.sampleName


class SangerZipFiles(models.Model):
    '''
    id, fileName(上传的sanger压缩包名称), sampleNumbers(压缩包内样本数), status(分析成功/失败), createTime
    '''
    STATUS_ITEMS = [(0,'上传成功'),(1,'上传失败')]
    ANALYSIS_ITEMS = [(0,'已分析'),(1,'未分析')]


    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    fileName = models.FileField(max_length=255, verbose_name="fileName", upload_to = "uploadSanger/",storage=FileStorage())
    sampleNumbers = models.PositiveIntegerField(verbose_name="sampleNumbers")
    status = models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name="status")
    analysisStatus = models.IntegerField(choices=ANALYSIS_ITEMS, default=1, verbose_name="analysisStauts")
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="createdTime")
    updateTime = models.DateTimeField(auto_now=True, verbose_name="updateTime")
    class Meta:
        verbose_name = verbose_name_plural = '数据上传'
    
