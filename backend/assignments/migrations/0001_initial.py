# Generated by Django 4.2.13 on 2024-07-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_date', models.DateField()),
                ('assignment_time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('arrival_time', models.TimeField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('parking_fee', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('notes', models.TextField(null=True)),
                ('round_trip_distance', models.IntegerField()),
                ('lep_name', models.CharField(max_length=100)),
                ('serviced_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_worked', models.DurationField()),
                ('submission_date', models.DateField()),
                ('approval_status', models.BooleanField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.assignment')),
            ],
        ),
    ]