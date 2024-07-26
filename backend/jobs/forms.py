from django import forms
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

class JobForm(forms.Form):
    job_id =  forms.CharField()
    job_date = forms.DateField()
    location = forms.CharField()
    practice_name = forms.CharField()
    language = forms.CharField()
    lep_name = forms.CharField()
    expected_duration = forms.DurationField()
    description = forms.CharField()