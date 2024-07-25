from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User
from .models import Interpreter

class InterpreterCreationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)
    ssn = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_interpreter = True
        if commit:
            user.save()
            interpreter = Interpreter(
                user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number'],
                ssn=self.cleaned_data['ssn']
            )
            interpreter.save()
        return user
