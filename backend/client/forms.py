from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField

from core.models import User, Address
from .models import Client, ClientApplicant
from . import constants as con


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
    # Address fields
    street_address = forms.CharField(max_length=100)
    apt_number = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=2, widget=forms.Select(choices=con.STATE_CHOICES))
    zip_code = forms.CharField(max_length=10)
    class Meta:
        model = Client
        fields = ['company_name', 'phone_number', 'fax_number']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize address fields if the interpreter has an associated address
        if self.instance.address:
            self.fields['street_address'].initial = self.instance.address.street_address
            self.fields['apt_number'].initial = self.instance.address.apt_number
            self.fields['city'].initial = self.instance.address.city
            self.fields['state'].initial = self.instance.address.state
            self.fields['zip_code'].initial = self.instance.address.zip_code

    def save(self, commit=True):
        client = super().save(commit=False)
        
        
        # Handle address saving or updating
        if not client.address:
            # Create a new Address if it doesn't exist
            address = Address(
                street_address=self.cleaned_data['street_address'],
                apt_number=self.cleaned_data.get('apt_number', ''),
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                zip_code=self.cleaned_data['zip_code']
            )
            address.save()
            client.address = address
        else:
            # Update existing Address
            client.address.street_address = self.cleaned_data['street_address']
            client.address.apt_number = self.cleaned_data.get('apt_number', '')
            client.address.city = self.cleaned_data['city']
            client.address.state = self.cleaned_data['state']
            client.address.zip_code = self.cleaned_data['zip_code']
            client.address.save()
        
        if commit:
            client.user.save()  # Save the User model
            client.save()       # Save the Interpreter model
            self.save_m2m()          # Save many-to-many fields
        
        return client

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