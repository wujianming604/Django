# Generated by Django 2.2.12 on 2020-04-22 07:24

import Sanger.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanger', '0008_auto_20200422_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sangersamples',
            name='abiPngUrl',
            field=models.ImageField(max_length=255, storage=Sanger.storage.FileStorage(), upload_to='uploadSanger/', verbose_name='abiPngUrl'),
        ),
        migrations.AlterField(
            model_name='sangerzipfiles',
            name='fileName',
            field=models.FileField(max_length=255, storage=Sanger.storage.FileStorage(), upload_to='uploadSanger/', verbose_name='fileName'),
        ),
    ]
