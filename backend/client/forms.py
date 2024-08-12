from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import Client, ClientApplicant

# class ClientCreationForm(UserCreationForm):
#     company_name = forms.CharField(max_length=255)
#     address = forms.CharField(widget=forms.Textarea)
#     phone_number = forms.CharField(max_length=15)
#     fax_number = forms.CharField(max_length=15, required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_client = True
#         if commit:
#             user.save()
#             client = Client(
#                 user=user,
#                 company_name=self.cleaned_data['company_name'],
#                 address=self.cleaned_data['address'],
#                 phone_number=self.cleaned_data['phone_number'],
#                 fax_number=self.cleaned_data['fax_number']
#             )
#             client.save()
#         return user

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company_name', 'phone_number', 'fax_number']

class ClientApplicantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                FloatingField("poc_first_name"),
                FloatingField("poc_last_name"),
                FloatingField("poc_phone_number"),
                FloatingField("poc_email_address"),
                FloatingField("company_name"),
                FloatingField("company_phone_number"),
                FloatingField("ceo_first_name"),
                FloatingField("ceo_last_name"),
                FloatingField("ceo_phone_number"),
                FloatingField("ceo_email_address"),
                FloatingField("street_address"),
                FloatingField("apt_number"),
                FloatingField("city"),
                FloatingField("state"),
                FloatingField("zip_code"),
                FloatingField("fax_number"),
                ButtonHolder(
                    Submit('submit', 'Signup', css_class='btn btn-primary')
                )
            )
    class Meta:
        model = ClientApplicant
        fields = "__all__"
        exclude = ['accept', 'decline']
        labels = {
            "poc_first_name": "Point of Contact's First Name",
            "poc_last_name": "Point of Contact's Last Name",
            "poc_mobile_phone": "Point of Contact's Phone Number",
            "poc_email_address": "Point of Contact's Email Address",
            
        }