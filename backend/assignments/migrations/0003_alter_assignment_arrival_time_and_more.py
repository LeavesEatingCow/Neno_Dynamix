# Generated by Django 4.2.13 on 2024-08-30 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='arrival_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='round_trip_distance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]