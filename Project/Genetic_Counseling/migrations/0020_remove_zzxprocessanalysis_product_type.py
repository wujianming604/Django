# Generated by Django 2.2.12 on 2021-01-12 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0019_auto_20210112_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zzxprocessanalysis',
            name='product_type',
        ),
    ]
