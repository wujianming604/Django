# Generated by Django 2.2.12 on 2021-09-15 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Genetic_Counseling', '0022_zkanalysis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processanalysis',
            old_name='second',
            new_name='second_check',
        ),
        migrations.RenameField(
            model_name='zzxprocessanalysis',
            old_name='second',
            new_name='second_check',
        ),
    ]
