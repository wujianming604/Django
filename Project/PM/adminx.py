import xadmin
# from django.contrib import admin
from .models import PM
from xadmin.views import ListAdminView
from xadmin.layout import Main, Fieldset, Row
from xadmin.plugins.fieldsplugin import FieldsPlugin

class PMAdmin(object):

    list_display = ('id', 'type_id', 'project_name', 'user_name', 'sample_name','kinsfolk_sample', 'product_type', 'sample_type', 'hospital', 'representative', 'rep_phone', 'send_time', 'receive_time', 'clinical_info', 'father_barcode', 'mather_barcode', 'other_barcode', 'kins_recevie_time', 'ajtk_receive_time', 'ajtk_sample_type', 'ajtk_qc_time', 'ajtk_library_time', 'predict_data', 'ajtk_data', 'data_analysis_time', 'coun_analysis_time', 'sanger_send_time', 'predict_sanger_time', 'receive_sanger_time', 'predict_report', 'docoter_report', 'counseling_yuyue', 'counseling_feedback', 'report_update_time', 'user_report', 'send_report_time', 'mark')
    search_fields = ['sample_name','user_name','type_id']
    list_filter = ['sample_name','user_name','type_id']
    show_detail_fields = ['user_name']
    list_per_page = 16
    show_bookmarks = False

    list_editable = ['sample_name','kinsfolk_sample', 'product_type', 'sample_type', 'hospital', 'representative', 'rep_phone', 'send_time', 'receive_time', 'clinical_info', 'father_barcode', 'mather_barcode', 'other_barcode', 'kins_recevie_time', 'ajtk_receive_time', 'ajtk_sample_type', 'ajtk_qc_time', 'ajtk_library_time', 'predict_data', 'ajtk_data', 'data_analysis_time', 'coun_analysis_time', 'sanger_send_time', 'predict_sanger_time', 'receive_sanger_time', 'predict_report', 'docoter_report', 'counseling_yuyue', 'counseling_feedback', 'report_update_time', 'user_report', 'send_report_time', 'mark']
    
    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    form_layout = (
        Fieldset("项目部",
                Row('type_id','project_name'),
                Row('sample_name','user_name'),
                Row('kinsfolk_sample','product_type'), 
                Row('sample_type','hospital'), 
                Row('representative','rep_phone'), 
                Row('send_time','predict_report'),
                Row('counseling_yuyue','send_report_time'),
                
        ),
        Fieldset("检验所",
                Row('receive_time',  'father_barcode'), 
                Row('mather_barcode', 'other_barcode'),
                'clinical_info',
                Row('kins_recevie_time', 'ajtk_receive_time'), 
                Row('ajtk_sample_type', 'ajtk_qc_time'), 
                Row('ajtk_library_time', 'predict_data'), 
                Row('sanger_send_time', 'predict_sanger_time'), 'receive_sanger_time'
        ),
        Fieldset("生信",
                Row('ajtk_data', 'data_analysis_time'),
                Row('docoter_report', 'report_update_time'), 'user_report'
        ),
        Fieldset("遗传咨询师",
                'coun_analysis_time','counseling_feedback'
        )
    )
    

xadmin.site.register(PM, PMAdmin)
