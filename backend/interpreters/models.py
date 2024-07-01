from django.db import models

# Create your models here.
class Interpreter(models.Model):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str
    ssn: str
    username: str
    password: str

    def accept_job(self):
        pass

    def submit_timesheet(self):
        pass

    def send_update(self):
        pass

    