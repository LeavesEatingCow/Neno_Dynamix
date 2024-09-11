from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from core.models import Address
from .models import Interpreter, Language, InterpreterApplicant
from . import constants as con

User = get_user_model()
# class InterpreterCreationForm(UserCreationForm):
#     address = forms.CharField(widget=forms.Textarea)
#     phone_number = forms.CharField(max_length=15)
#     languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_interpreter = True
#         if commit:
#             user.save()
#             interpreter = Interpreter(
#                 user=user,
#                 address=self.cleaned_data['address'],
#                 phone_number=self.cleaned_data['phone_number'],
#             )
#             interpreter.save()
#             interpreter.languages.set(self.cleaned_data['languages'])
#         return user


class InterpreterProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    # Address fields
    street_address = forms.CharField(max_length=100)
    apt_number = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=2, widget=forms.Select(choices=con.STATE_CHOICES))
    zip_code = forms.CharField(max_length=10)
    
    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Interpreter
        fields = ['phone_number', 'languages']  # Only include Interpreter fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

        # Initialize address fields if the interpreter has an associated address
        if self.instance.address:
            self.fields['street_address'].initial = self.instance.address.street_address
            self.fields['apt_number'].initial = self.instance.address.apt_number
            self.fields['city'].initial = self.instance.address.city
            self.fields['state'].initial = self.instance.address.state
            self.fields['zip_code'].initial = self.instance.address.zip_code

    def save(self, commit=True):
        interpreter = super().save(commit=False)
        
        # Save the User data (first name, last name, email)
        interpreter.user.first_name = self.cleaned_data['first_name']
        interpreter.user.last_name = self.cleaned_data['last_name']
        interpreter.user.email = self.cleaned_data['email']
        
        # Handle address saving or updating
        if not interpreter.address:
            # Create a new Address if it doesn't exist
            address = Address(
                street_address=self.cleaned_data['street_address'],
                apt_number=self.cleaned_data.get('apt_number', ''),
                city=self.cleaned_data['city'],
                state=self.cleaned_data['state'],
                zip_code=self.cleaned_data['zip_code']
            )
            address.save()
            interpreter.address = address
        else:
            # Update existing Address
            interpreter.address.street_address = self.cleaned_data['street_address']
            interpreter.address.apt_number = self.cleaned_data.get('apt_number', '')
            interpreter.address.city = self.cleaned_data['city']
            interpreter.address.state = self.cleaned_data['state']
            interpreter.address.zip_code = self.cleaned_data['zip_code']
            interpreter.address.save()
        
        if commit:
            interpreter.user.save()  # Save the User model
            interpreter.save()       # Save the Interpreter model
            self.save_m2m()          # Save many-to-many fields
        
        return interpreter
    

class InterpreterApplicantForm(forms.ModelForm):

    class Meta:
        model = InterpreterApplicant
        fields = "__all__"
        exclude = ['accept', 'decline']
        labels = {
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'mobile_phone': 'Mobile Phone',
            'email_address': 'Email Address',
            'street_address': 'Street Address',
            'apt_number': 'Apt#',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip',
            'authorized_to_work': 'Are you authorized to work in the United States?',
            'native_language': 'What is your native or first language?',
            'fluently_spoken_languages_count': 'How many languages do you fluently speak?',
            'spoken_languages': 'Rank all spoken languages in order of fluency (From advanced to beginner level)',
            'fluently_written_languages_count': 'How many languages can you perfectly write and read?',
            'written_languages': 'Rank all written languages in order of capability (From advanced to beginner level)',
            'language_services_experience': 'How many years of language services experience do you have?',
            'interpretation_strength': 'What is your interpretation strength? (Select Multiple Check Boxes if necessary)',
            'interpretation_field': 'What is your main interpretation field? (Select Multiple Check Boxes if necessary)',
            'comfortable_interpreting_from': 'Are you more comfortable interpreting from:',
            'document_translation_service': 'Have you ever performed any document translation service?',
            'comfortable_translating_from': 'Are you more comfortable translating from:',
            'interpretation_translation_training': 'Have you completed any Interpretation/Translation training, certification or degree?',
            'document_translation_specialization': 'What is your document translation specialization?',
            'most_translated_document_type': 'What type of documents are you translating the most?',
            'translation_software_tools': 'What translation software or tools are you using?',
            'words_translated_per_hour': 'How many words can you translate per hour?',
            'landline_phone_service': 'Do you have landline phone service at home?',
            'car_ownership': 'Do you own a car?',
            'home_office': 'Do you have an office or a quiet dedicated room at home?',
            'computer_ownership': 'Do you have a computer desktop or laptop?',
            'internet_skills': 'Rank your internet skills level:',
            'resume': 'Upload Resume',
        }
        widgets = {
            'authorized_to_work': forms.RadioSelect,
            'document_translation_service': forms.RadioSelect,
            'interpretation_translation_training': forms.RadioSelect,
            'landline_phone_service': forms.RadioSelect,
            'car_ownership': forms.RadioSelect,
            'home_office': forms.RadioSelect,
            'computer_ownership': forms.RadioSelect,
            'currently_working': forms.RadioSelect,
        }
            






