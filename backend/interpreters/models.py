from django.db import models
from core.models import User, Address
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

from . import constants as con

class Interpreter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name =  models.CharField(max_length=50)
    # last_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=15)
    # email =  models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    languages = models.ManyToManyField('Language', related_name='interpreters')

    rate_of_pay = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2
    )

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class InterpreterApplicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=15)
    email_address = models.EmailField()
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=con.STATE_CHOICES)
    zip_code = models.CharField(max_length=10)
    authorized_to_work = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    native_language = models.CharField(max_length=50)
    fluently_spoken_languages_count = models.CharField(max_length=10, choices=con.LANGUAGE_COUNT_CHOICES)
    spoken_languages = models.TextField()
    fluently_written_languages_count = models.CharField(max_length=10, choices=con.LANGUAGE_COUNT_CHOICES)
    written_languages = models.TextField()
    language_services_experience = models.CharField(max_length=20, choices=con.EXPERIENCE_CHOICES)
    interpretation_strength = models.CharField(max_length=50, choices=con.INTERPRETATION_STRENGTH_CHOICES)
    interpretation_field = models.CharField(max_length=50, choices=con.INTERPRETATION_FIELD_CHOICES)
    comfortable_interpreting_from = models.CharField(max_length=50)
    document_translation_service = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    comfortable_translating_from = models.CharField(max_length=50)
    interpretation_translation_training = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    document_translation_specialization = models.CharField(max_length=50, choices=con.TRANSLATION_SPECIALIZATION_CHOICES)
    most_translated_document_type = models.CharField(max_length=50)
    translation_software_tools = models.CharField(max_length=50)
    words_translated_per_hour = models.CharField(max_length=50)
    landline_phone_service = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    car_ownership = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    home_office = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    computer_ownership = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    internet_skills = models.CharField(max_length=50, choices=con.SKILL_LEVEL_CHOICES)
    mobile_app_skills = models.CharField(max_length=50, choices=con.SKILL_LEVEL_CHOICES)
    cell_phone_os = models.CharField(max_length=50, choices=con.PHONE_OS_CHOICES)
    currently_working = models.BooleanField(choices=con.BOOL_CHOICES, default=False)
    current_language_services = models.TextField()
    current_rate = models.CharField(max_length=50)
    rate_expectation = models.CharField(max_length=50)
    payment_methods = models.CharField(max_length=50, choices=con.PAYMENT_METHOD_CHOICES)
    job_references = models.TextField()
    referrals = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
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

            address = Address.objects.create(
                street_address=instance.street_address,
                apt_number=instance.apt_number,
                city=instance.city,
                state=instance.state,
                zip_code=instance.zip_code,
            )
            address.save()

            interpreter = Interpreter.objects.create(
                user=user,
                phone_number=instance.mobile_phone,
                address=address,
            )
            interpreter.save()
            
post_save.connect(create_accepted_interpreter_user, sender=InterpreterApplicant)

