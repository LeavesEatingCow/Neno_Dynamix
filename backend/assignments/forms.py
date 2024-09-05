from django import forms
from .models import Assignment

class AssignmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssignmentUpdateForm, self).__init__(*args, **kwargs)
        # self.fields['notes'].required = False
        for field in self.fields:
            self.fields[field].required = False

    class Meta:
        model = Assignment
        fields = ['arrival_time', 'start_time', 'end_time', 'parking_fee', 'notes', 'round_trip_distance']
        widgets = {
            'arrival_time' : forms.TimeInput(attrs={'type': 'time'}),
            'start_time' : forms.TimeInput(attrs={'type': 'time'}),
            'end_time' : forms.TimeInput(attrs={'type': 'time'})
        }