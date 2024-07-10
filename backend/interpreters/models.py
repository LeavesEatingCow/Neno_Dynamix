from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Interpreter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name =  models.CharField(max_length=100, blank=False)
    # last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    # email =  models.EmailField()
    address =  models.CharField(max_length=100, blank=False)
    ssn =  models.CharField(max_length=100, blank=False)
    # username =  models.CharField(max_length=100, blank=False)
    # password =  models.CharField(max_length=100, blank=False)

    def accept_job(self):
        pass

    def submit_timesheet(self):
        pass

    def send_update(self):
        pass

    def __str__(self) -> str:
        return self.user.username
