# Generated by Django 2.2.12 on 2020-12-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0007_auto_20201116_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pm',
            name='father_barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='父亲样本条码核对'),
        ),
        migrations.AlterField(
            model_name='pm',
            name='mather_barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='母亲样本条码核对'),
        ),
        migrations.AlterField(
            model_name='pm',
            name='other_barcode',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='其他样本条码核对'),
        ),
    ]