# Generated by Django 4.2.13 on 2024-08-30 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_expected_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_time',
            field=models.TimeField(default=datetime.time(1, 4, 59, 58774)),
            preserve_default=False,
        ),
    ]
