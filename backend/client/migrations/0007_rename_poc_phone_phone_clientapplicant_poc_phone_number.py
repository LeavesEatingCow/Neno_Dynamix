# Generated by Django 4.2.13 on 2024-08-01 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_rename_ceo_phone_phone_clientapplicant_ceo_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientapplicant',
            old_name='poc_phone_phone',
            new_name='poc_phone_number',
        ),
    ]
