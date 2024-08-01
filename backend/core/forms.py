from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from core.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        field_classes = {"username": UsernameField}


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("password",)