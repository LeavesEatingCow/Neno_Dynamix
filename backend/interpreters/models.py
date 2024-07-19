from django.db import models
from core.models import User
class Interpreter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=15)
    email =  models.EmailField()
    address =  models.TextField()
    ssn = models.CharField(max_length=11)

    def accept_job(self):
        pass

    def submit_timesheet(self):
        pass

    def send_update(self):
        pass

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
