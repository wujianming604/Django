# Generated by Django 2.2.12 on 2020-09-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessAnalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sample_id', models.IntegerField(verbose_name='序号')),
                ('sample_name', models.CharField(max_length=50, verbose_name='样本编号')),
                ('user_name', models.CharField(max_length=10, verbose_name='患者姓名')),
                ('hospital', models.CharField(max_length=50, verbose_name='送检医院')),
                ('area', models.CharField(max_length=25, verbose_name='大区')),
                ('representative', models.CharField(max_length=10, verbose_name='代表')),
                ('product_type', models.CharField(max_length=10, verbose_name='产品类型')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='送检日期')),
                ('receive_time', models.DateTimeField(auto_now_add=True, verbose_name='收样日期')),
                ('predict_data', models.DateTimeField(auto_now_add=True, verbose_name='预计下机时间')),
                ('predict_report', models.DateTimeField(auto_now_add=True, verbose_name='预计出报告时间')),
                ('data_complete_analysis', models.DateTimeField(auto_now_add=True, verbose_name='原始数据分析完成时间')),
                ('first_check', models.CharField(max_length=50, verbose_name='一审人+完成时间')),
                ('sanger', models.CharField(max_length=25, verbose_name='Sanger验证位点')),
                ('second', models.CharField(max_length=50, verbose_name='二审人+完成时间')),
                ('sanger_check', models.CharField(max_length=25, verbose_name='Sanger验证位点是否一致')),
                ('sanger_send_time', models.CharField(max_length=25, verbose_name='Sanger测序送测时间')),
                ('sanger_complete_time', models.CharField(max_length=25, verbose_name='Sanger测序完成时间')),
                ('cnv', models.CharField(max_length=50, verbose_name='CNV分析结果')),
                ('report_writer', models.CharField(max_length=50, verbose_name='报告撰写人+完成时间')),
                ('report_check', models.CharField(max_length=50, verbose_name='报告审核人+完成时间')),
                ('report_time', models.CharField(max_length=20, verbose_name='报告完成时间')),
                ('report_day', models.CharField(max_length=10, verbose_name='报告周期/自然日')),
                ('mark', models.TextField(default=-9, verbose_name='备注')),
            ],
            options={
                'verbose_name': '遗传分析流程进度',
                'verbose_name_plural': '遗传分析流程进度',
            },
        ),
    ]
