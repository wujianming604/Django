import xadmin
# from django.contrib import admin
from .models import ProcessAnalysis, zzxProcessAnalysis, SampleInfo, GeneDisease, ZKAnalysis

class ProcessAnalysisAdmin(object):
    #list_display = ('id','sample_id','sample_name','user_name','hospital','area','representative','product_type','send_time','receive_time','predict_data','predict_report','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','report_day','mark')
    list_display = ('sample_id','user_name','age','sex','mark','sample_name','other_sample','hospital','product_type','send_time','receive_time','predict_data','predict_report','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','doctor_report','user_report','report_day')
    search_fields = ['sample_id','sample_name','user_name','product_type','hospital','mark']
    list_filter = ['sample_id','sample_name','user_name','product_type','hospital','mark']

    show_detail_fields = ['user_name']
    list_per_page = 16
    show_bookmarks = False
    show_all_rel_details = False
    #默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态。将preserve_filters设为False后，则会返回未过滤状态。
    #preserve_filters = True
    
    
    #只读字段
    readonly_fields = []

    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    #list_editable 设置默认可编辑字段
    list_editable = ['age','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','doctor_report','user_report','report_day','mark']

class ZKAnalysisAdmin(object):
    list_display = ('sample_id','birth','sex','product_type','user_name','mark','sample_name','other_sample','hospital','send_time','receive_time','predict_data','predict_report','data_complete_analysis','send_data_to_zk','send_clinical_to_zk','zk_analysis_finish','send_sanger_to_test','sanger_complete_time','send_sanger_to_zk','zk_report','doctor_report','user_report','report_day')
    search_fields = ['sample_id','sample_name','user_name','product_type','hospital','mark']
    list_filter = ['sample_id','sample_name','user_name','product_type','hospital','mark']

    show_detail_fields = ['user_name']
    list_per_page = 16
    show_bookmarks = False
    show_all_rel_details = False
    #默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态。将preserve_filters设为False后，则会返回未过滤状态。
    #preserve_filters = True
    
    #只读字段
    readonly_fields = []

    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    #list_editable 设置默认可编辑字段
    list_editable = ['user_name','birth','sex','mark','sample_name','other_sample','hospital','product_type','send_time','receive_time','predict_data','predict_report','data_complete_analysis','send_data_to_zk','send_clinical_to_zk','zk_analysis_finish','send_sanger_to_test','sanger_complete_time','send_sanger_to_zk','zk_report','doctor_report','user_report','report_day']


class zzxProcessAnalysisAdmin(object):
    #list_display = ('id','sample_id','sample_name','user_name','hospital','area','representative','product_type','send_time','receive_time','predict_data','predict_report','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','report_day','mark')
    list_display = ('sample_id','user_name','age','sex','mark','sample_name','other_sample','hospital','send_time','receive_time','predict_data','predict_report','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','doctor_report','user_report','report_day')
    search_fields = ['sample_id','sample_name','user_name','hospital']
    list_filter = ['sample_id','sample_name','user_name','hospital']

    show_detail_fields = ['user_name']
    list_per_page = 16
    show_bookmarks = False
    show_all_rel_details = False
    #默认情况下，当你对目标进行创建、编辑或删除操作后，页面会依然保持原来的过滤状态。将preserve_filters设为False后，则会返回未过滤状态。
    #preserve_filters = True
    
    #只读字段
    readonly_fields = []

    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    #list_editable 设置默认可编辑字段
    list_editable = ['age','data_complete_analysis','first_check','sanger','second','sanger_check','sanger_send_time','sanger_complete_time','cnv','report_writer','report_check','report_time','doctor_report','user_report','report_day','mark']


class SampleInfoAdmin(object):
    list_display = ('sample_id', 'Sample_name','User_name','Sex','Report_result','Exon_table1','Exon_table2','Exon_table3','ChrM','CNV','Acmg','Report_diagnose','Doctor_diagnose','Region','Detect_project','Send_time','Received_time','Cal_report_time','Real_report_time','PaternalInfoId','PaternalResult','MaternalInfoId','MaternalResult','CompatriotInfoId','CompatriotResult')
    #list_display = ('sample_id', 'Sample_name','Sample_proper','User_name','Sex','Birth','Age','Clinical', 'Report_result','Exon_table1','Exon_table2','Exon_table3','ChrM','CNV','Acmg','Report_diagnose','Doctor_diagnose','Organize_name','Region','Product','Detect_project','Send_time','Received_time','Cal_report_time','Real_report_time','PaternalInfoId','PaternalResult','MaternalInfoId','MaternalResult','CompatriotInfoId','CompatriotResult')
    search_fields = ['sample_id', 'Sample_name', 'Sample_proper','Sex','Exon_table1','Exon_table2','Exon_table3','Organize_name','Detect_project']
    list_filter = ['sample_id', 'Sample_name', 'Sample_proper','Sex','Exon_table1','Exon_table2','Exon_table3','Organize_name','Detect_project']

    show_detail_fields = ['Sample_name']
    list_per_page = 16
    show_bookmarks = False
    show_all_rel_details = False

    
    #只读字段
    readonly_fields = []

    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    #list_editable 设置默认可编辑字段
    list_editable = ['Clinical', 'Report_result','Exon_table1','Exon_table2','Exon_table3','ChrM','CNV','Acmg','Report_diagnose','Doctor_diagnose','Organize_name','Region','Product','Detect_project','Send_time','Received_time','Cal_report_time','Real_report_time','PaternalInfoId','PaternalResult','MaternalInfoId','MaternalResult','CompatriotInfoId','CompatriotResult']

class GeneDiseaseAdmin(object):
    #查询结果字段
    list_display = ('id', 'gene', 'genetic_model', 'omim', 'morbidity', 'morbidity_age', 'penetrance', 'clinical_intervention', 'case_manage', 'clinical_monitoring',  'created_time')
    #搜索框
    search_fields = ['gene', 'genetic_model']
    #过滤框
    list_filter = ['gene', 'genetic_model']
    # list_exclude = ['updateTime']
    #列表可直接修改字段
    show_bookmarks = False
    # 每页显示的数据行数
    list_per_page = 16
    list_editable = ['gene', 'disease', 'genetic_model', 'morbidity', 'morbidity_age','penetrance', 'clinical_feature', 'clinical_intervention', 'case_manage', 'clinical_monitoring', 'avoid', 'risk_assessment', 'reason']
    fields = ('gene', 'disease', 'genetic_model', 'morbidity', 'clinical_feature', 'clinical_intervention', 'case_manage', 'clinical_monitoring', 'avoid', 'risk_assessment', 'reason','other')


xadmin.site.register(GeneDisease, GeneDiseaseAdmin)
xadmin.site.register(SampleInfo, SampleInfoAdmin)
xadmin.site.register(ProcessAnalysis, ProcessAnalysisAdmin)
xadmin.site.register(zzxProcessAnalysis, zzxProcessAnalysisAdmin)
xadmin.site.register(ZKAnalysis, ZKAnalysisAdmin)