import xadmin
# from django.contrib import admin
from .models import QC


class QCAdmin(object):
    # list_display = ('id', 'sample_id', 'sample_name', 'raw_bases', 'map_bases', 'dedup_bases', 'dedup_reads', 'dedup_rate', 'bed_size', 'target_bases', 'target_reads', 'capture_rate', 'mean_depth_raw', 'mean_depth', 'cds_bed_size', 'cds_target_bases', 'cds_capture_rate', 'cds_mean_depth_raw', 'cds_mean_depth', 'cnv_bed_size', 'cnv_target_bases', 'cnv_capture_rate', 'cnv_mean_depth_raw', 'cnv_mean_depth', 'chrM_bed_size', 'chrM_target_bases', 'chrM_capture_rate', 'chrM_mean_depth_raw', 'chrM_mean_depth', 'cover1X', 'cover10X', 'cover50X', 'cover100X', 'cover200X', 'cover500X')
    list_display = ('id', 'sample_id', 'sample_name', 'raw_bases', 'map_rate', 'dedup_rate', 'capture_rate', 'mean_depth_raw', 'cds_capture_rate', 'chrM_mean_depth', 'cover1X')
    search_fields = ['sample_id', 'sample_name']
    list_filter = ['sample_id', 'sample_name']
    list_per_page = 20
    show_bookmarks = False
    
    #只读字段
    readonly_fields = ['id', 'sample_id', 'sample_name', 'raw_bases', 'map_bases', 'dedup_bases', 'dedup_reads', 'dedup_rate', 'bed_size', 'target_bases', 'target_reads', 'capture_rate', 'mean_depth_raw', 'mean_depth', 'cds_bed_size', 'cds_target_bases', 'cds_capture_rate', 'cds_mean_depth_raw', 'cds_mean_depth', 'cnv_bed_size', 'cnv_target_bases', 'cnv_capture_rate', 'cnv_mean_depth_raw', 'cnv_mean_depth', 'chrM_bed_size', 'chrM_target_bases', 'chrM_capture_rate', 'chrM_mean_depth_raw', 'chrM_mean_depth', 'cover1X', 'cover10X', 'cover50X', 'cover100X', 'cover200X', 'cover500X']

    # fields = ('sampleName', 'chrom', 'pos', 'genoType', 'abiFileUrl', 'abiPngUrl',)
    

xadmin.site.register(QC, QCAdmin)