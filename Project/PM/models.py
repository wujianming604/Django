from django.contrib.auth.models import User
from django.db import models



class PM(models.Model):
    
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)     # 序号
    type_id = models.CharField(max_length=10, null=True, blank=True, verbose_name="亚类序号")
    project_name = models.CharField(max_length=10, verbose_name="项目名称")
    sample_name = models.CharField(max_length=50, verbose_name="样本编号")
    user_name = models.CharField(max_length=20, verbose_name="患者姓名")
    kinsfolk_sample = models.CharField(max_length=255, null=True, blank=True, verbose_name="亲属送样情况")
    product_type = models.CharField(max_length=50, verbose_name="产品类型")
    sample_type = models.CharField(max_length=10, verbose_name="样本类型")
    hospital = models.CharField(max_length=50, null=True, blank=True, verbose_name="送检医院")
    representative = models.CharField(max_length=10, null=True, blank=True, verbose_name="代表姓名")
    rep_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="联系电话")
    send_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="样本送检时间")
    receive_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="样本接收时间")
    clinical_info = models.TextField(default='', blank=True, null=True, verbose_name="有无临床信息")
    father_barcode = models.CharField(max_length=50, null=True, blank=True, verbose_name="父亲样本条码核对")
    mather_barcode = models.CharField(max_length=50, null=True, blank=True, verbose_name="母亲样本条码核对")
    other_barcode = models.CharField(max_length=255, null=True, blank=True, verbose_name="其他样本条码核对")
    kins_recevie_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="亲属样本到达时间")
    ajtk_receive_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="外包收样时间")
    ajtk_sample_type = models.CharField(max_length=25, null=True, blank=True, verbose_name="外包样本类型")
    ajtk_qc_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="样本质检完成时间")
    ajtk_library_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="文库构建完成时间")
    predict_data = models.CharField(max_length=25, null=True, blank=True, verbose_name="预计数据下机")
    ajtk_data = models.CharField(max_length=25, null=True, blank=True, verbose_name="外包交付时间")
    data_analysis_time =  models.CharField(max_length=25, null=True, blank=True, verbose_name="数据分析完成时间")
    coun_analysis_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="遗传分析完成时间")
    sanger_send_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="Sanger验证送出时间")
    predict_sanger_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="预计Sanger验证交付时间")
    receive_sanger_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="Sanger验证交付时间")
    predict_report = models.CharField(max_length=25, null=True, blank=True, verbose_name="预计出报告时间")
    docoter_report = models.CharField(max_length=25, null=True, blank=True, verbose_name="医生版报告出具时间")
    counseling_yuyue = models.CharField(max_length=25, null=True, blank=True, verbose_name="遗传咨询预约时间")
    counseling_feedback = models.TextField(default='', blank=True, null=True, verbose_name="遗传咨询反馈结果")
    report_update_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="报告更新时间")
    user_report = models.CharField(max_length=25, null=True, blank=True, verbose_name="患者版报告出具时间")
    send_report_time = models.CharField(max_length=25, null=True, blank=True, verbose_name="报告寄送时间")
    mark =  models.TextField( null=True, blank=True, verbose_name="备注")

    # sample_id = models.IntegerField(verbose_name="sampleId")
    # sample_name = models.CharField(max_length=50, verbose_name="sampleName")
    # map_reads = models.TextField(default='', verbose_name="mappingReads")
    # map_rate = models.FloatField(default='', verbose_name="mappingRate")
 
    class Meta:
        verbose_name = verbose_name_plural = '进度表'
        ordering = ('-id',)
    
    def __str__(self):
        return self.sample_name
