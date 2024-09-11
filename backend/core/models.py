from django.db import models
from django.contrib.auth.models import AbstractUser

from interpreters import constants as con


# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_interpreter = models.BooleanField(default=False)
    password_changed = models.BooleanField(default=False)

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=con.STATE_CHOICES)
    zip_code = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"