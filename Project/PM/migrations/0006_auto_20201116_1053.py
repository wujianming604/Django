# Generated by Django 2.2.12 on 2020-11-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0005_auto_20201109_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pm',
            options={'ordering': ('-id',), 'verbose_name': '进度表', 'verbose_name_plural': '进度表'},
        ),
        migrations.AddField(
            model_name='pm',
            name='type_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='亚类序号'),
        ),
    ]
