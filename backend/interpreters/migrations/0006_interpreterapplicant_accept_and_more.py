# Generated by Django 4.2.13 on 2024-07-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpreters', '0005_interpreterapplicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='interpreterapplicant',
            name='accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interpreterapplicant',
            name='decline',
            field=models.BooleanField(default=False),
        ),
    ]