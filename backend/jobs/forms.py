from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit, Button
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import Job
from interpreters.models import Language
class JobModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                FloatingField('client_job_id', css_class='form-control'),
                FloatingField('job_date', css_class='form-control'),
                FloatingField('job_time', css_class='form-control'),
                FloatingField('location', css_class='form-control'),
                FloatingField('practice_name', css_class='form-control'),
                FloatingField('language', css_class='form-control'),
                FloatingField('lep_name', css_class='form-control'),
                FloatingField('expected_duration', css_class='form-control'),
                FloatingField('description', css_class='form-control'),
                css_class='modal-body'
            ),
            Div(
                Button(
                    'cancel', 'Cancel', css_class='btn btn-secondary', **{'data-bs-dismiss': 'modal'}
                ),
                ButtonHolder(
                    Submit('submit', 'Save', css_class='btn btn-primary')
                ),
                css_class='modal-footer',
                css_id='form-footer'  # Adding custom id if needed
            )
        )
    class Meta:
        model = Job
        # Fields you want to display
        fields = (
            "client_job_id", 
            "job_date",
            "job_time",
            "location",
            "practice_name",
            "language",
            "lep_name",
            "expected_duration",
            "description",

        )
        widgets = {
            'language': forms.Select(choices=Language.objects.all()),
            'job_date': forms.DateInput(attrs={'type': 'date'}),
            'job_time': forms.TimeInput(attrs={'type': 'time'})
        }
    
    def clean_client_job_id(self):
        client_job_id = self.cleaned_data.get('client_job_id')
        if not self.instance.pk:
            # If creating a new job, check if client_job_id already exists
            if Job.objects.filter(client_job_id=client_job_id).exists():
                raise ValidationError("A job with this client_job_id already exists.")
        else:
            # If updating, ensure it's not changed to another job's client_job_id
            if Job.objects.filter(client_job_id=client_job_id).exclude(pk=self.instance.pk).exists():
                raise ValidationError("A job with this client_job_id already exists.")

        return client_job_id

class JobForm(forms.Form):
    job_id =  forms.CharField()
    job_date = forms.DateField()
    location = forms.CharField()
    practice_name = forms.CharField()
    language = forms.CharField()
    lep_name = forms.CharField()
    expected_duration = forms.DurationField()
    description = forms.CharField()