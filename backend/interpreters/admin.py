from django.contrib import admin
from .models import Interpreter, Language, InterpreterApplicant

# Register your models here.
admin.site.register(Interpreter)
admin.site.register(InterpreterApplicant)
admin.site.register(Language)