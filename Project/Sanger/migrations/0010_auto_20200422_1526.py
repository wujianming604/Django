# Generated by Django 2.2.12 on 2020-04-22 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanger', '0009_auto_20200422_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sangerzipfiles',
            old_name='updateTime',
            new_name='update_time',
        ),
    ]
