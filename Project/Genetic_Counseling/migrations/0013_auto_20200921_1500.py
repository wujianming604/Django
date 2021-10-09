# Generated by Django 2.2.12 on 2020-09-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0012_auto_20200918_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampleinfo',
            name='doctor_report',
        ),
        migrations.RemoveField(
            model_name='sampleinfo',
            name='user_report',
        ),
        migrations.AddField(
            model_name='processanalysis',
            name='doctor_report',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='医生版上传日期'),
        ),
        migrations.AddField(
            model_name='processanalysis',
            name='user_report',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='患者版上传日期'),
        ),
    ]