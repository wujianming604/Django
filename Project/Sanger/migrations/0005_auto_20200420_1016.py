# Generated by Django 2.2.12 on 2020-04-20 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sanger', '0004_sangerzipfiles_analysis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sangerzipfiles',
            old_name='analysis',
            new_name='analysisStatus',
        ),
    ]
