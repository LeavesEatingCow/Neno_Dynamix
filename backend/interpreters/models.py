from django.db import models
from core.models import User
class Interpreter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name =  models.CharField(max_length=50)
    # last_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=15)
    # email =  models.EmailField()
    address =  models.TextField()
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
