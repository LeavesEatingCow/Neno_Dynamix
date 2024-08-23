from django import forms
from django.core.exceptions import ValidationError
from .models import Job
from interpreters.models import Language
class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        # Fields you want to display
        fields = (
            "client_job_id", 
            "job_date",
            "location",
            "practice_name",
            "language",
            "lep_name",
            "expected_duration",
            "description",

        )
        widgets = {
            'language': forms.Select(choices=Language.objects.all())
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