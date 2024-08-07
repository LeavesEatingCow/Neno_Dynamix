# Generated by Django 4.2.13 on 2024-07-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        ('interpreters', '0001_initial'),
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='interpreter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interpreters.interpreter'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='interpreter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interpreters.interpreter'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='job',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='jobs.job'),
        ),
    ]
