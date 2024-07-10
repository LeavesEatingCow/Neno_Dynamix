from django.db import models

# Create your models here.
class Assignment(models.Model):
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    job = models.OneToOneField("jobs.Job", unique=True, on_delete=models.DO_NOTHING)
    assignment_date = models.DateField()
    assignment_time = models.TimeField()
    location = models.CharField(max_length=100, blank=False)
    language = models.CharField(max_length=100, blank=False)
    arrival_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    parking_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    notes = models.TextField(null=True)
    round_trip_distance = models.IntegerField()
    lep_name = models.CharField(max_length=100)
    serviced_name = models.CharField(max_length=100)
    # signature = models.ImageField()

class Timesheet(models.Model):
    assignment = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    hours_worked = models.DurationField()
    submission_date = models.DateField()
    approval_status = models.BooleanField()