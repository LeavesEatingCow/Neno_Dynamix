# Generated by Django 4.2.13 on 2024-09-06 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_rename_job_assignment_referring_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='referring_job',
            new_name='job',
        ),
    ]
