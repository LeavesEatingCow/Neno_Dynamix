from django.db import models
from core.models import User
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField()
    rate_of_pay = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.company_name}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class CEO(models.Model):
    client = models.OneToOneField("Client", unique=True, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.EmailField()

class Contact(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.EmailField()