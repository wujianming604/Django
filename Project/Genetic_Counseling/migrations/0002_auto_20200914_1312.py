# Generated by Django 2.2.12 on 2020-09-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processanalysis',
            name='data_complete_analysis',
            field=models.CharField(max_length=25, verbose_name='原始数据分析完成时间'),
        ),
    ]