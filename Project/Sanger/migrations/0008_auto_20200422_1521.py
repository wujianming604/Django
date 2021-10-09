# Generated by Django 2.2.12 on 2020-04-22 07:21

import Sanger.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanger', '0007_auto_20200422_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sangerzipfiles',
            old_name='update_time',
            new_name='updateTime',
        ),
        migrations.AlterField(
            model_name='sangersamples',
            name='abiPngUrl',
            field=models.ImageField(storage=Sanger.storage.FileStorage(), upload_to='uploadSanger/', verbose_name='abiPngUrl'),
        ),
        migrations.AlterField(
            model_name='sangerzipfiles',
            name='fileName',
            field=models.FileField(storage=Sanger.storage.FileStorage(), upload_to='uploadSanger/', verbose_name='fileName'),
        ),
    ]