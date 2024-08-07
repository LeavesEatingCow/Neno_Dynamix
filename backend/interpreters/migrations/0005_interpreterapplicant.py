# Generated by Django 4.2.13 on 2024-07-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpreters', '0004_remove_interpreter_ssn'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterpreterApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=100)),
                ('apt_number', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('authorized_to_work', models.BooleanField()),
                ('native_language', models.CharField(max_length=50)),
                ('fluently_spoken_languages_count', models.CharField(choices=[('1-2', '1 - 2 languages'), ('3-4', '3 - 4 languages'), ('4+', 'More than 4 languages')], max_length=10)),
                ('spoken_languages', models.TextField()),
                ('fluently_written_languages_count', models.CharField(choices=[('1-2', '1 - 2 languages'), ('3-4', '3 - 4 languages'), ('4+', 'More than 4 languages')], max_length=10)),
                ('written_languages', models.TextField()),
                ('language_services_experience', models.CharField(choices=[('none', 'None'), ('less_than_a_year', 'Less than a year'), ('1-3', '1-3 years'), ('3-5', '3-5 years'), ('5+', 'More than 5 years')], max_length=20)),
                ('interpretation_strength', models.CharField(choices=[('none', "I don't necessarily have a strength"), ('on_site', 'On-Site interpretation'), ('over_phone', 'Over-The-Phone interpretation'), ('escort', 'Escort interpretation'), ('consecutive', 'Consecutive interpretation'), ('simultaneous', 'Simultaneous interpretation')], max_length=50)),
                ('interpretation_field', models.CharField(choices=[('none', "I don't have any"), ('medical', 'Medical'), ('schools', 'Schools'), ('legal', 'Legal/Court'), ('social', 'Social'), ('other', 'Other')], max_length=50)),
                ('comfortable_interpreting_from', models.CharField(max_length=50)),
                ('document_translation_service', models.BooleanField()),
                ('comfortable_translating_from', models.CharField(max_length=50)),
                ('interpretation_translation_training', models.BooleanField()),
                ('document_translation_specialization', models.CharField(choices=[('none', "I don't have any specialization"), ('standard', 'Standard Translation'), ('technical', 'Technical Translation'), ('transcreation', 'Transcreation'), ('other', 'Other')], max_length=50)),
                ('most_translated_document_type', models.CharField(max_length=50)),
                ('translation_software_tools', models.CharField(max_length=50)),
                ('words_translated_per_hour', models.CharField(max_length=50)),
                ('landline_phone_service', models.BooleanField()),
                ('car_ownership', models.BooleanField()),
                ('home_office', models.BooleanField()),
                ('computer_ownership', models.BooleanField()),
                ('internet_skills', models.CharField(choices=[('poor', 'Poor'), ('average', 'Average'), ('excellent', 'Excellent')], max_length=50)),
                ('mobile_app_skills', models.CharField(choices=[('poor', 'Poor'), ('average', 'Average'), ('excellent', 'Excellent')], max_length=50)),
                ('cell_phone_os', models.CharField(choices=[('ios', 'IOS (iPhone)'), ('android', 'Android'), ('microsoft', 'Microsoft'), ('blackberry', 'Blackberry'), ('other', 'Other')], max_length=50)),
                ('currently_working', models.BooleanField()),
                ('current_language_services', models.TextField()),
                ('current_rate', models.CharField(max_length=50)),
                ('rate_expectation', models.CharField(max_length=50)),
                ('payment_methods', models.CharField(choices=[('direct_deposit', 'Direct Deposit'), ('check', 'Check'), ('cash', 'Cash'), ('other', 'Other')], max_length=50)),
                ('job_references', models.TextField()),
                ('referrals', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
