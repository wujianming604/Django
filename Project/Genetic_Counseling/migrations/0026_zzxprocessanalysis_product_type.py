# Generated by Django 2.2.12 on 2022-07-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0025_auto_20220222_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='zzxprocessanalysis',
            name='product_type',
            field=models.CharField(max_length=50, null=True, verbose_name='产品类型'),
        ),
    ]
