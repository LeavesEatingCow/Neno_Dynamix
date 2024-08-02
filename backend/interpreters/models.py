from django.db import models
from core.models import User
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

class Interpreter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name =  models.CharField(max_length=50)
    # last_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=15)
    # email =  models.EmailField()
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    languages = models.ManyToManyField('Language', related_name='interpreters')

    def accept_job(self):
        pass

    def submit_timesheet(self):
        pass

    def send_update(self):
        pass

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
from django.db import models

class InterpreterApplicant(models.Model):
    STATE_CHOICES = [
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
    ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
    ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
    ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
    ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
    ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
    ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ]

    
    LANGUAGE_COUNT_CHOICES = [
        ('1-2', '1 - 2 languages'),
        ('3-4', '3 - 4 languages'),
        ('4+', 'More than 4 languages'),
    ]
    
    EXPERIENCE_CHOICES = [
        ('none', 'None'),
        ('less_than_a_year', 'Less than a year'),
        ('1-3', '1-3 years'),
        ('3-5', '3-5 years'),
        ('5+', 'More than 5 years'),
    ]
    
    INTERPRETATION_STRENGTH_CHOICES = [
        ('none', 'I don\'t necessarily have a strength'),
        ('on_site', 'On-Site interpretation'),
        ('over_phone', 'Over-The-Phone interpretation'),
        ('escort', 'Escort interpretation'),
        ('consecutive', 'Consecutive interpretation'),
        ('simultaneous', 'Simultaneous interpretation'),
    ]
    
    INTERPRETATION_FIELD_CHOICES = [
        ('none', 'I don\'t have any'),
        ('medical', 'Medical'),
        ('schools', 'Schools'),
        ('legal', 'Legal/Court'),
        ('social', 'Social'),
        ('other', 'Other'),
    ]
    
    TRANSLATION_SPECIALIZATION_CHOICES = [
        ('none', 'I don\'t have any specialization'),
        ('standard', 'Standard Translation'),
        ('technical', 'Technical Translation'),
        ('transcreation', 'Transcreation'),
        ('other', 'Other'),
    ]
    
    PHONE_OS_CHOICES = [
        ('ios', 'IOS (iPhone)'),
        ('android', 'Android'),
        ('microsoft', 'Microsoft'),
        ('blackberry', 'Blackberry'),
        ('other', 'Other'),
    ]
    
    SKILL_LEVEL_CHOICES = [
        ('poor', 'Poor'),
        ('average', 'Average'),
        ('excellent', 'Excellent'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('direct_deposit', 'Direct Deposit'),
        ('check', 'Check'),
        ('cash', 'Cash'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=15)
    email_address = models.EmailField()
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=10)
    authorized_to_work = models.BooleanField()
    native_language = models.CharField(max_length=50)
    fluently_spoken_languages_count = models.CharField(max_length=10, choices=LANGUAGE_COUNT_CHOICES)
    spoken_languages = models.TextField()
    fluently_written_languages_count = models.CharField(max_length=10, choices=LANGUAGE_COUNT_CHOICES)
    written_languages = models.TextField()
    language_services_experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    interpretation_strength = models.CharField(max_length=50, choices=INTERPRETATION_STRENGTH_CHOICES)
    interpretation_field = models.CharField(max_length=50, choices=INTERPRETATION_FIELD_CHOICES)
    comfortable_interpreting_from = models.CharField(max_length=50)
    document_translation_service = models.BooleanField()
    comfortable_translating_from = models.CharField(max_length=50)
    interpretation_translation_training = models.BooleanField()
    document_translation_specialization = models.CharField(max_length=50, choices=TRANSLATION_SPECIALIZATION_CHOICES)
    most_translated_document_type = models.CharField(max_length=50)
    translation_software_tools = models.CharField(max_length=50)
    words_translated_per_hour = models.CharField(max_length=50)
    landline_phone_service = models.BooleanField()
    car_ownership = models.BooleanField()
    home_office = models.BooleanField()
    computer_ownership = models.BooleanField()
    internet_skills = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES)
    mobile_app_skills = models.CharField(max_length=50, choices=SKILL_LEVEL_CHOICES)
    cell_phone_os = models.CharField(max_length=50, choices=PHONE_OS_CHOICES)
    currently_working = models.BooleanField()
    current_language_services = models.TextField()
    current_rate = models.CharField(max_length=50)
    rate_expectation = models.CharField(max_length=50)
    payment_methods = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    job_references = models.TextField()
    referrals = models.TextField(blank=True, null=True)
    accept = models.BooleanField(default=False)
    decline = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def create_accepted_interpreter_user(sender, instance, created, **kwargs):
    if instance.accept:
            user = User.objects.create(
                username=instance.email_address,
                first_name=instance.first_name,
                last_name=instance.last_name,
                email=instance.email_address,
                is_interpreter=True
            )
            password = get_random_string(length=32)
            user.set_password(password)
            user.save(update_fields=['password'])   
            print(password)
            interpreter = Interpreter.objects.create(
                user=user,
                phone_number=instance.mobile_phone,
                street_address=instance.street_address,
                apt_number=instance.apt_number,
                city=instance.city,
                state=instance.state, 
                zip_code=instance.zip_code,
            )
            
post_save.connect(create_accepted_interpreter_user, sender=InterpreterApplicant)

