from django.contrib.auth.models import User
from django.db import models


class ProcessAnalysis(models.Model):

    '''
    送检样本贝安臻流程进度表。
    列表title：

    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(verbose_name="序号")
    mark =  models.TextField( null=True, verbose_name="备注")
    sex = models.CharField(max_length=25, blank=True, null=True, verbose_name="性别")
    age = models.CharField( max_length=50, blank=True, null=True, verbose_name="出生日期")
    sample_name = models.CharField(max_length=50, verbose_name="样本编号")
    user_name = models.CharField(max_length=30, verbose_name="患者姓名")
    other_sample = models.CharField(max_length=255, null=True, verbose_name="亲属样本条码")
    hospital = models.CharField(max_length=50, verbose_name="送检医院")
    area = models.CharField(max_length=25, verbose_name="大区")
    representative = models.CharField(max_length=25, verbose_name="代表")
    product_type = models.CharField(max_length=50, verbose_name="产品类型")
    send_time = models.CharField(max_length=25, null=True, verbose_name="送检日期")
    receive_time = models.CharField(max_length=25, null=True, verbose_name="收样日期")
    predict_data = models.CharField(max_length=25, null=True, verbose_name="预计下机时间")
    predict_report = models.CharField(max_length=25, null=True, verbose_name="预计出报告时间")
    data_complete_analysis = models.CharField( max_length=25, null=True, verbose_name="原始数据分析完成时间")
    first_check = models.CharField( max_length=100, null=True, verbose_name="一审人+完成时间")
    sanger = models.CharField(max_length=100, null=True, verbose_name="Sanger验证位点")
    second_check = models.CharField(max_length=100, null=True, verbose_name="二审人+完成时间")
    sanger_check = models.CharField(max_length=100, null=True, verbose_name="Sanger验证位点是否一致")
    sanger_send_time = models.CharField(max_length=100, null=True, verbose_name="Sanger测序送测时间")
    sanger_complete_time = models.CharField(max_length=100, null=True, verbose_name="Sanger测序完成时间")
    cnv = models.TextField( null=True, verbose_name="CNV分析结果")
    report_writer = models.CharField(max_length=100, null=True, verbose_name="报告撰写人+完成时间")
    report_check = models.CharField(max_length=100, null=True, verbose_name="报告审核人+完成时间")
    report_time = models.CharField(max_length=50, null=True, verbose_name="报告完成时间")
    doctor_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="医生版上传日期")
    user_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="患者版上传日期")
    report_day = models.CharField(max_length=25, null=True, verbose_name="报告周期/自然日")
    re_ana_date = models.CharField(max_length=25, null=True, verbose_name="重分析日期")
    re_ana_result = models.CharField(max_length=100, null=True, verbose_name="重分析结果")
    
    class Meta:
        verbose_name = verbose_name_plural = '贝安臻流程进度'
        ordering = ('-sample_id',)

    def __str__(self):
        return self.sample_name

class zzxProcessAnalysis(models.Model):

    '''
    送检样本臻智选流程进度表。
    列表title：

    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(verbose_name="序号")
    mark =  models.TextField( null=True, verbose_name="备注")
    sex = models.CharField(max_length=25, blank=True, null=True, verbose_name="性别")
    age = models.CharField( max_length=50, blank=True, null=True, verbose_name="出生日期")
    sample_name = models.CharField(max_length=50, verbose_name="样本编号")
    user_name = models.CharField(max_length=10, verbose_name="患者姓名")
    other_sample = models.CharField(max_length=255, null=True, verbose_name="亲属样本条码")
    hospital = models.CharField(max_length=50, verbose_name="送检医院")
    area = models.CharField(max_length=25, verbose_name="大区")
    representative = models.CharField(max_length=10, verbose_name="代表")
    product_type = models.CharField(max_length=50, null=True, verbose_name="产品类型")
    send_time = models.CharField(max_length=25, null=True, verbose_name="送检日期")
    receive_time = models.CharField(max_length=25, null=True, verbose_name="收样日期")
    predict_data = models.CharField(max_length=25, null=True, verbose_name="预计下机时间")
    predict_report = models.CharField(max_length=25, null=True, verbose_name="预计出报告时间")
    data_complete_analysis = models.CharField( max_length=25, null=True, verbose_name="原始数据分析完成时间")
    first_check = models.CharField( max_length=100, null=True, verbose_name="一审人+完成时间")
    sanger = models.CharField(max_length=100, null=True, verbose_name="Sanger验证位点")
    second_check = models.CharField(max_length=100, null=True, verbose_name="二审人+完成时间")
    sanger_check = models.CharField(max_length=100, null=True, verbose_name="Sanger验证位点是否一致")
    sanger_send_time = models.CharField(max_length=100, null=True, verbose_name="Sanger测序送测时间")
    sanger_complete_time = models.CharField(max_length=100, null=True, verbose_name="Sanger测序完成时间")
    cnv = models.TextField( null=True, verbose_name="CNV分析结果")
    report_writer = models.CharField(max_length=100, null=True, verbose_name="报告撰写人+完成时间")
    report_check = models.CharField(max_length=100, null=True, verbose_name="报告审核人+完成时间")
    report_time = models.CharField(max_length=50, null=True, verbose_name="报告完成时间")
    doctor_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="医生版上传日期")
    user_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="患者版上传日期")
    report_day = models.CharField(max_length=10, null=True, verbose_name="报告周期/自然日")
    
    class Meta:
        verbose_name = verbose_name_plural = '臻智选流程进度'
        ordering = ('-sample_id',)

    def __str__(self):
        return self.sample_name


class SampleInfo(models.Model):
    
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(blank=True, null=True,verbose_name="序号")
    Sample_name = models.CharField(max_length = 50, blank=True, null=True, verbose_name="患者编号")
    Sample_proper = models.CharField(max_length = 50, blank=True, null=True, verbose_name="样本性质")
    User_name = models.CharField(max_length = 50, blank=True, null=True, verbose_name="患者姓名")
    Sex = models.CharField(max_length = 5, blank=True, null=True, verbose_name="性别")
    Birth = models.CharField(max_length = 20, blank=True, null=True, verbose_name="出生日期")
    Age = models.CharField(max_length = 20, blank=True, null=True, verbose_name="年龄")
    Clinical = models.TextField(blank=True, null=True, verbose_name="临床表现")     #
    Report_result = models.TextField(blank=True, null=True, verbose_name="报告结果")     #
    Exon_table1 = models.TextField(blank=True, null=True, verbose_name="外显子组表1")   #
    Exon_table2 = models.TextField(blank=True, null=True, verbose_name="外显子组表2")   #
    Exon_table3 = models.TextField(blank=True, null=True, verbose_name="外显子组表3")   #
    ChrM = models.TextField(blank=True, null=True, verbose_name="线粒体基因组") #
    CNV = models.TextField(blank=True, null=True, verbose_name="CNV")   #
    Acmg = models.TextField(blank=True, null=True, verbose_name="ACMG") #
    Report_diagnose = models.TextField(blank=True, null=True, verbose_name="初步诊断")    #
    Doctor_diagnose = models.TextField(blank=True, null=True, verbose_name="遗传咨询后诊断")    #
    Organize_name = models.CharField(max_length = 50, blank=True, null=True, verbose_name="医院")
    Region = models.CharField(max_length = 50, blank=True, null=True, verbose_name="大区")
    Product = models.CharField(max_length = 50, blank=True, null=True, verbose_name="产品")
    Detect_project = models.CharField(max_length = 50, blank=True, null=True, verbose_name="检测项目")
    Send_time = models.CharField(max_length = 20, blank=True, null=True, verbose_name="送检日期")
    Received_time = models.CharField(max_length = 20, blank=True, null=True, verbose_name="收样日期")
    Cal_report_time = models.CharField(max_length = 20, blank=True, null=True, verbose_name="预计报告日期")
    Real_report_time = models.CharField(max_length = 20, blank=True, null=True, verbose_name="报告日期")
    PaternalInfoId = models.CharField(max_length = 50, blank=True, null=True, verbose_name="父亲样本编号")
    PaternalResult = models.TextField(blank=True, null=True, verbose_name="父亲验证结果")   #
    MaternalInfoId = models.CharField(max_length = 50, blank=True, null=True, verbose_name="母亲样本编号")
    MaternalResult = models.TextField(blank=True, null=True, verbose_name="母亲验证结果")   #
    CompatriotInfoId = models.TextField(blank=True, null=True, verbose_name="同胞样本编号")
    CompatriotResult = models.TextField(blank=True, null=True, verbose_name="同胞验证结果") #
    Update_time = models.DateTimeField(auto_now_add=True, verbose_name="updateTime")

    class Meta:
        verbose_name = verbose_name_plural = 'SampleInfo'
        ordering = ('-sample_id',)
    
    def __str__(self):
        return self.Sample_name


class GeneDisease(models.Model):
    '''
    列表title：基因、疾病、遗传模式、发病率、外显率、临床表现、临床干预、患者管理、临床监测、需要避免的情况、家系成员患病风险评估、可能存在临床检测阴性的原因
    
    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    Gene = models.CharField(max_length = 50, blank=True, null=True, verbose_name="Gene")
    Gene_OMIM_ID = models.CharField(max_length = 50, blank=True, null=True,  verbose_name="Gene_OMIM_ID")
    Gene_Description_CH = models.TextField(blank=True, null=True, verbose_name="Gene_Description_CH")
    OMIM_Disease_CH = models.TextField(blank=True, null=True, verbose_name="OMIM_Disease_CH")
    OMIM_Disease = models.TextField(blank=True, null=True, verbose_name="OMIM_Disease")
    Disease_OMIM_ID = models.CharField(max_length = 50,blank=True, null=True, verbose_name="Disease_OMIM_ID")
    OMIM_Inhert = models.CharField(max_length = 50,blank=True, null=True, verbose_name="OMIM_Inhert")
    Disease_Description_CH = models.TextField(blank=True, null=True,verbose_name="Disease_Description_CH")
    HPO_All_Terms = models.TextField(blank=True, null=True,verbose_name="HPO_All_Terms")
    CHPO_All_Terms = models.TextField(blank=True, null=True,verbose_name="CHPO_All_Terms")
    OMIM_Clinical_Synopses = models.TextField(blank=True, null=True,verbose_name="OMIM_Clinical_Synopses")
    OMIM_Clinical_Synopses_CH = models.TextField(blank=True, null=True, verbose_name="OMIM_Clinical_Synopses_CH")
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="createdTime")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="updateTime")

    class Meta:
        verbose_name = verbose_name_plural = 'GeneDisease'
    
    def __str__(self):
        return self.Gene


class ZKAnalysis(models.Model):
    '''
    列表title：患者姓名、出生日期、性别、备注、样本编号、亲属样本条码、送检医院、产品类型、送检日期、收样日期、预计下机时间、预计出报告时间、原始数据分析完成时间、数据发送到中抗时间、发送临床信息到中抗时间、中抗分析完成时间、恩元Sanger测序送测时间、Sanger测序完成时间、Sanger测序结果发送到中抗时间、中抗报告撰写完成时间、医生版上传日期、患者版上传日期、报告周期/自然日
    
    '''
    # 自增主键, 这里不能设置default属性，负责执行save的时候就不会新增而是修改元素
    id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(verbose_name="序号")
    user_name = models.CharField(max_length=10, verbose_name="患者姓名")
    birth = models.CharField(max_length = 20, blank=True, null=True, verbose_name="出生日期")
    sex = models.CharField(max_length=25, blank=True, null=True, verbose_name="性别")
    mark =  models.TextField( null=True, verbose_name="备注")
    sample_name = models.CharField(max_length=50, verbose_name="样本编号")
    other_sample = models.CharField(max_length=255, null=True, verbose_name="亲属样本条码")
    hospital = models.CharField(max_length=50, verbose_name="送检医院")
    product_type = models.CharField(max_length=50, verbose_name="产品类型")
    send_time = models.CharField(max_length=25, null=True, verbose_name="送检日期")
    receive_time = models.CharField(max_length=25, null=True, verbose_name="收样日期")
    predict_data = models.CharField(max_length=25, null=True, verbose_name="预计下机时间")
    predict_report = models.CharField(max_length=25, null=True, verbose_name="预计出报告时间")
    data_complete_analysis = models.CharField( max_length=25, null=True, verbose_name="原始数据分析完成时间")
    send_data_to_zk = models.CharField( max_length=30, null=True, verbose_name="数据发送到中抗时间")
    send_clinical_to_zk = models.CharField(max_length=30, null=True, verbose_name="发送临床信息到中抗时间")
    zk_analysis_finish = models.CharField(max_length=30, null=True, verbose_name="中抗分析完成时间")
    send_sanger_to_test = models.CharField(max_length=30, null=True, verbose_name="恩元Sanger测序送测时间")
    sanger_complete_time = models.CharField(max_length=30, null=True, verbose_name="Sanger测序完成时间")
    send_sanger_to_zk = models.CharField(max_length=30, null=True, verbose_name="Sanger测序结果发送到中抗时间")
    zk_report = models.CharField(max_length=30, null=True, verbose_name="中抗报告撰写完成时间")
    doctor_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="医生版上传日期")
    user_report = models.CharField(max_length = 25, blank=True, null=True, verbose_name="患者版上传日期")
    report_day = models.CharField(max_length=30, null=True, verbose_name="报告周期/自然日")

    class Meta:
        verbose_name = verbose_name_plural = 'ZKAnalysis'
    
    def __str__(self):
        return self.sample_name
