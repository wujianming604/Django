# Generated by Django 2.2.12 on 2022-01-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0009_auto_20210128_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pm',
            name='rep_phone',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='联系电话'),
        ),
    ]
