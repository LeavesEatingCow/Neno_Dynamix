from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Interpreter, Language

User = get_user_model()
class InterpreterCreationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)
    ssn = forms.CharField(max_length=15, required=False)
    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple)

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
            interpreter.languages.set(self.cleaned_data['languages'])
        return user


class InterpreterProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Interpreter
        fields = ['phone_number', 'address', 'languages']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        interpreter = super().save(commit=False)
        interpreter.user.first_name = self.cleaned_data['first_name']
        interpreter.user.last_name = self.cleaned_data['last_name']
        interpreter.user.email = self.cleaned_data['email']
        if commit:
            interpreter.user.save()
            interpreter.save()
            self.save_m2m()
        return interpreter