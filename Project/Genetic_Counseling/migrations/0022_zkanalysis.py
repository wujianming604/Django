# Generated by Django 2.2.12 on 2021-03-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0021_auto_20210207_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZKAnalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sample_id', models.IntegerField(verbose_name='序号')),
                ('user_name', models.CharField(max_length=10, verbose_name='患者姓名')),
                ('birth', models.CharField(blank=True, max_length=20, null=True, verbose_name='出生日期')),
                ('sex', models.CharField(blank=True, max_length=25, null=True, verbose_name='性别')),
                ('mark', models.TextField(null=True, verbose_name='备注')),
                ('sample_name', models.CharField(max_length=50, verbose_name='样本编号')),
                ('other_sample', models.CharField(max_length=255, null=True, verbose_name='亲属样本条码')),
                ('hospital', models.CharField(max_length=50, verbose_name='送检医院')),
                ('product_type', models.CharField(max_length=25, verbose_name='产品类型')),
                ('send_time', models.CharField(max_length=25, null=True, verbose_name='送检日期')),
                ('receive_time', models.CharField(max_length=25, null=True, verbose_name='收样日期')),
                ('predict_data', models.CharField(max_length=25, null=True, verbose_name='预计下机时间')),
                ('predict_report', models.CharField(max_length=25, null=True, verbose_name='预计出报告时间')),
                ('data_complete_analysis', models.CharField(max_length=25, null=True, verbose_name='原始数据分析完成时间')),
                ('send_data_to_zk', models.CharField(max_length=30, null=True, verbose_name='数据发送到中抗时间')),
                ('send_clinical_to_zk', models.CharField(max_length=30, null=True, verbose_name='发送临床信息到中抗时间')),
                ('zk_analysis_finish', models.CharField(max_length=30, null=True, verbose_name='中抗分析完成时间')),
                ('send_sanger_to_test', models.CharField(max_length=30, null=True, verbose_name='恩元Sanger测序送测时间')),
                ('sanger_complete_time', models.CharField(max_length=30, null=True, verbose_name='Sanger测序完成时间')),
                ('send_sanger_to_zk', models.CharField(max_length=30, null=True, verbose_name='Sanger测序结果发送到中抗时间')),
                ('zk_report', models.CharField(max_length=30, null=True, verbose_name='中抗报告撰写完成时间')),
                ('doctor_report', models.CharField(blank=True, max_length=25, null=True, verbose_name='医生版上传日期')),
                ('user_report', models.CharField(blank=True, max_length=25, null=True, verbose_name='患者版上传日期')),
                ('report_day', models.CharField(max_length=30, null=True, verbose_name='报告周期/自然日')),
            ],
            options={
                'verbose_name': 'ZKAnalysis',
                'verbose_name_plural': 'ZKAnalysis',
            },
        ),
    ]