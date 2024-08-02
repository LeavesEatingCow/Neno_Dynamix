from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User
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