from django.db import models
from django.db.models.signals import post_save
from core.models import User
# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
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

class Contact(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=100, blank=False)
    last_name =  models.CharField(max_length=100, blank=False)
    phone_number =  models.CharField(max_length=100, blank=False)
    email =  models.EmailField()


# def post_user_created_signal(sender, instance, created, **kwargs):
#     if instance.is_client:
#             Client.objects.create(user=instance)
#     print(instance, created)

# post_save.connect(post_user_created_signal, sender=User)
