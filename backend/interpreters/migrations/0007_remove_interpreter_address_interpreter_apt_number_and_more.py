# Generated by Django 4.2.13 on 2024-07-31 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpreters', '0006_interpreterapplicant_accept_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interpreter',
            name='address',
        ),
        migrations.AddField(
            model_name='interpreter',
            name='apt_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='interpreter',
            name='city',
            field=models.CharField(default='Atlanta', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interpreter',
            name='state',
            field=models.CharField(default='Georgia', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interpreter',
            name='street_address',
            field=models.CharField(default='Cathcart', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interpreter',
            name='zip_code',
            field=models.CharField(default=30045, max_length=10),
            preserve_default=False,
        ),
    ]
