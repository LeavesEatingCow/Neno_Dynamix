from django.contrib import admin
from .models import Client, CEO, Contact, ClientApplicant

# Register your models here.
admin.site.register(Client)
admin.site.register(CEO)
admin.site.register(Contact)
admin.site.register(ClientApplicant)