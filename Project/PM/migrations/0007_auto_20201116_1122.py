# Generated by Django 2.2.12 on 2020-11-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0006_auto_20201116_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pm',
            name='kinsfolk_sample',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='亲属送样情况'),
        ),
    ]