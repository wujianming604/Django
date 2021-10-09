# Generated by Django 2.2.12 on 2020-05-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sample_id', models.IntegerField(verbose_name='sampleId')),
                ('sample_name', models.CharField(max_length=50, verbose_name='sampleName')),
                ('raw_bases', models.TextField(default=-9, verbose_name='rawBases')),
                ('raw_reads', models.TextField(default=-9, verbose_name='rawReads')),
                ('clean_reads', models.TextField(default=-9, verbose_name='cleanReads')),
                ('map_bases', models.TextField(default=-9, verbose_name='mappingBases')),
                ('map_reads', models.TextField(default=-9, verbose_name='mappingReads')),
                ('map_rate', models.FloatField(default=-9, verbose_name='mappingRate')),
                ('dedup_bases', models.TextField(default=-9, verbose_name='dedupBases')),
                ('dedup_reads', models.TextField(default=-9, verbose_name='dedupReads')),
                ('dedup_rate', models.FloatField(default=-9, verbose_name='dedupRate')),
                ('bed_size', models.TextField(default=-9, verbose_name='bedSize')),
                ('target_bases', models.TextField(default=-9, verbose_name='targetBases')),
                ('target_reads', models.TextField(default=-9, verbose_name='teargetReads')),
                ('capture_rate', models.FloatField(default=-9, verbose_name='captureRate')),
                ('mean_depth_raw', models.FloatField(default=-9, verbose_name='meanDepthRaw')),
                ('mean_depth', models.FloatField(default=-9, verbose_name='meanDepth')),
                ('cds_bed_size', models.TextField(default=-9, verbose_name='cdsBedSize')),
                ('cds_target_bases', models.TextField(default=-9, verbose_name='cdsTargetBases')),
                ('cds_capture_rate', models.FloatField(default=-9, verbose_name='cdsCaptureRate')),
                ('cds_mean_depth_raw', models.FloatField(default=-9, verbose_name='cdsMeanDepthRaw')),
                ('cds_mean_depth', models.FloatField(default=-9, verbose_name='cdsMeanDepth')),
                ('cnv_bed_size', models.TextField(default=-9, verbose_name='cnvBedSize')),
                ('cnv_target_bases', models.TextField(default=-9, verbose_name='cnvTargetBases')),
                ('cnv_capture_rate', models.FloatField(default=-9, verbose_name='cnvCaptureRate')),
                ('cnv_mean_depth_raw', models.FloatField(default=-9, verbose_name='cnvMeanDepthRaw')),
                ('cnv_mean_depth', models.FloatField(default=-9, verbose_name='cnvMeanDepth')),
                ('chrM_bed_size', models.TextField(default=-9, verbose_name='chrMBedSize')),
                ('chrM_target_bases', models.TextField(default=-9, verbose_name='chrMTargetBases')),
                ('chrM_capture_rate', models.FloatField(default=-9, verbose_name='chrMCaptureRate')),
                ('chrM_mean_depth_raw', models.FloatField(default=-9, verbose_name='chrMMeanDepthRaw')),
                ('chrM_mean_depth', models.FloatField(default=-9, verbose_name='chrMMeanDepth')),
                ('cover1X', models.FloatField(default=-9, verbose_name='1X')),
                ('cover10X', models.FloatField(default=-9, verbose_name='10X')),
                ('cover50X', models.FloatField(default=-9, verbose_name='50X')),
                ('cover100X', models.FloatField(default=-9, verbose_name='100X')),
                ('cover200X', models.FloatField(default=-9, verbose_name='200X')),
                ('cover500X', models.FloatField(default=-9, verbose_name='500X')),
            ],
            options={
                'verbose_name': 'QC',
                'verbose_name_plural': 'QC',
            },
        ),
    ]
