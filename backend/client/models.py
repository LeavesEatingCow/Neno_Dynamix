from django.db import models
from django.db.models.signals import post_save
from core.models import User
from django.utils.crypto import get_random_string
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    rate_of_pay = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.company_name}'

class CEO(models.Model):
    client = models.OneToOneField("Client", unique=True, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.EmailField()

    def __str__(self):
         return f"{self.first_name} {self.last_name}"

class Contact(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.EmailField()

    def __str__(self):
         return f"{self.first_name} {self.last_name}"


class ClientApplicant(models.Model):
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
    
    company_name = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=15)
    ceo_first_name = models.CharField(max_length=50)
    ceo_last_name = models.CharField(max_length=50)
    ceo_phone_number = models.CharField(max_length=15)
    ceo_email_address = models.EmailField()
    poc_first_name = models.CharField(max_length=50)
    poc_last_name = models.CharField(max_length=50)
    poc_phone_number = models.CharField(max_length=15)
    poc_email_address = models.EmailField()
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=10)
    fax_number = models.CharField(max_length=15, blank=True, null=True)
    accept = models.BooleanField(default=False)
    decline = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.company_name}"
    

def create_accepted_client_user(sender, instance, created, **kwargs):
    if instance.accept:
            user = User.objects.create(
                username=instance.poc_email_address,                
                is_client=True
            )
            password = get_random_string(length=32)
            user.set_password(password)
            user.save(update_fields=['password'])   
            print(password)
            client = Client.objects.create(
                user=user,
                company_name=instance.company_name,
                phone_number=instance.company_phone_number,
                street_address=instance.street_address,
                apt_number=instance.apt_number,
                city=instance.city,
                state=instance.state, 
                zip_code=instance.zip_code,
                fax_number=instance.fax_number,
            )
            client.save()
            ceo = CEO.objects.create(
                client=client,
                first_name=instance.ceo_first_name,
                last_name=instance.ceo_last_name,
                phone_number=instance.ceo_phone_number,
                email=instance.ceo_email_address,
            )
            contact = Contact.objects.create(
                client=client,
                first_name=instance.poc_first_name,
                last_name=instance.poc_last_name,
                phone_number=instance.poc_phone_number,
                email=instance.poc_email_address,
            )
            contact.save()

            
post_save.connect(create_accepted_client_user, sender=ClientApplicant)