from django.db import models

# Create your models here.
class Interpreter(models.Model):
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.CharField(max_length=100, blank=False)
    address =  models.CharField(max_length=100, blank=False)
    ssn =  models.CharField(max_length=100, blank=False)
    username =  models.CharField(max_length=100, blank=False)
    password =  models.CharField(max_length=100, blank=False)

    def accept_job(self):
        pass

    def submit_timesheet(self):
        pass

    def send_update(self):
        pass

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'