from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_interpreter = models.BooleanField(default=False)
    password_changed = models.BooleanField(default=False)