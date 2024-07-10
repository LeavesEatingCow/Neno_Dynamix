from django.db import models

# Create your models here.
class Client(models.Model):
    company_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    fax_number = models.CharField(max_length=100)
    start_date = models.DateField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rate_of_pay = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

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