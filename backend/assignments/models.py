import googlemaps
import json
from django.db import models
from django.conf import settings


# Create your models here.
class Assignment(models.Model):
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    job = models.OneToOneField("jobs.Job", null=True, on_delete=models.SET_NULL)
    assignment_date = models.DateField(blank=True, null=True)
    assignment_time = models.TimeField(blank=True, null=True)
    location = models.ForeignKey("core.Address", on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=100)
    arrival_time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    parking_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True, null=True)
    round_trip_distance = models.IntegerField(default=0)
    lep_name = models.CharField(max_length=100)
    serviced_name = models.CharField(max_length=100)
    # signature = models.ImageField(upload_to='signatures/', null=True, blank=True)

    def save(self, *args, **kwargs):
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        distance = gmaps.distance_matrix(str(self.interpreter.address), str(self.location), units="imperial")['rows'][0]['elements'][0]['distance']['text'].split()[0]
        self.round_trip_distance = int(float(distance))
        print(self.round_trip_distance)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.interpreter} assigned to {self.job}"
            
class Timesheet(models.Model):
    assignment = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    hours_worked = models.DurationField()
    submission_date = models.DateField()
    approval_status = models.BooleanField()