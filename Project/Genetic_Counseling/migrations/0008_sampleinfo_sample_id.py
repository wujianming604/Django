# Generated by Django 2.2.12 on 2020-09-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0007_auto_20200916_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleinfo',
            name='sample_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='序号'),
        ),
    ]
