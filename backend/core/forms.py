from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
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

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                FloatingField("username"),
                FloatingField("password"),
                ButtonHolder(
                    Submit('submit', 'Login', css_class='btn btn-primary')
                )
            )