from django.contrib import admin
from .models import Interpreter, Language

# Register your models here.
admin.site.register(Interpreter)
admin.site.register(Language)