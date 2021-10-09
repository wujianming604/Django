from django.contrib.auth.models import User
from django.db import models


class DD_QC(models.Model):
    '''
    列表title：id, sample_id, sample_name,raw bases,mapping bases,dedup bases,dedup reads,dedup rate(%),bed size,target bases,target reads,capture rate(%),mean depth raw,mean depth,cds bed size,cds target bases,cds capture rate(%),cds mean depth raw, cds mean depth,chrM bed size,chrM target bases,chrM capture rate(%),chrM mean depth raw, chrM mean depth,1X coverage rate,10X coverage rate,50X coverage rate,100X coverage rate,200X coverage rate,500X coverage rate

    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(verbose_name="sampleId")
    sample_name = models.CharField(max_length=50, verbose_name="sampleName")
    raw_bases = models.TextField(default=-9, verbose_name="rawBases")
    raw_reads = models.TextField(default=-9, verbose_name="rawReads")
    clean_reads = models.TextField(default=-9, verbose_name="cleanReads")
    map_bases = models.TextField(default=-9, verbose_name="mappingBases")
    map_reads = models.TextField(default=-9, verbose_name="mappingReads")
    map_rate = models.FloatField(default=-9, verbose_name="mappingRate")
    dedup_bases = models.TextField(default=-9, verbose_name="dedupBases")
    dedup_reads = models.TextField(default=-9, verbose_name="dedupReads")
    dedup_rate = models.FloatField(default=-9, verbose_name="dedupRate")
    bed_size = models.TextField(default=-9, verbose_name="bedSize")
    target_bases = models.TextField(default=-9, verbose_name="targetBases")
    target_reads = models.TextField(default=-9, verbose_name="teargetReads")
    capture_rate = models.FloatField(default=-9, verbose_name="captureRate")
    mean_depth_raw = models.FloatField(default=-9, verbose_name="meanDepthRaw")
    mean_depth = models.FloatField(default=-9, verbose_name="meanDepth")
    cds_bed_size = models.TextField(default=-9, verbose_name="cdsBedSize")
    cds_target_bases = models.TextField(default=-9, verbose_name="cdsTargetBases")
    cds_capture_rate = models.FloatField(default=-9, verbose_name="cdsCaptureRate")
    cds_mean_depth_raw = models.FloatField(default=-9, verbose_name="cdsMeanDepthRaw")
    cds_mean_depth = models.FloatField(default=-9, verbose_name="cdsMeanDepth")
    chrM_bed_size = models.TextField(default=-9, verbose_name="chrMBedSize")
    chrM_target_bases = models.TextField(default=-9, verbose_name="chrMTargetBases")
    chrM_capture_rate = models.FloatField(default=-9, verbose_name="chrMCaptureRate")
    chrM_mean_depth_raw = models.FloatField(default=-9, verbose_name="chrMMeanDepthRaw")
    chrM_mean_depth = models.FloatField(default=-9, verbose_name="chrMMeanDepth")
    cover1X = models.FloatField(default=-9, verbose_name="1X")
    cover10X = models.FloatField(default=-9, verbose_name="10X")
    cover20X = models.FloatField(default=-9, verbose_name="20X")
    cover50X = models.FloatField(default=-9, verbose_name="50X")
    cover100X = models.FloatField(default=-9, verbose_name="100X")
    cover200X = models.FloatField(default=-9, verbose_name="200X")
    cover500X = models.FloatField(default=-9, verbose_name="500X")
 
    class Meta:
        verbose_name = verbose_name_plural = 'QC'
    
    def __str__(self):
        return self.sample_name
