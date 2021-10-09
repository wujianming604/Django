from django.contrib.auth.models import User
from django.db import models


class MT_QC(models.Model):
    '''

    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(verbose_name="sampleId")
    sample_name = models.CharField(max_length=50, verbose_name="sampleName")
    raw_bases = models.TextField(default=-9, verbose_name="rawBases")
    raw_reads = models.TextField(default=-9, verbose_name="rawReads")
    clean_reads = models.TextField(default=-9, verbose_name="cleanReads")
    map_reads = models.TextField(default=-9, verbose_name="mappingReads")
    map_rate = models.FloatField(default=-9, verbose_name="mappingRate")
    dedup_reads = models.TextField(default=-9, verbose_name="dedupReads")
    dedup_rate = models.FloatField(default=-9, verbose_name="dedupRate")
    target_reads = models.TextField(default=-9, verbose_name="teargetReads")
    capture_rate = models.FloatField(default=-9, verbose_name="captureRate")
    mean_depth_raw = models.FloatField(default=-9, verbose_name="meanDepthRaw")
    mean_depth = models.FloatField(default=-9, verbose_name="meanDepth")
 
    class Meta:
        verbose_name = verbose_name_plural = 'MT_QC'
    
    def __str__(self):
        return self.sample_name
