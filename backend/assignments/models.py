from django.db import models

# Create your models here.
class Assignment(models.Model):
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    job = models.OneToOneField("jobs.Job", unique=True, on_delete=models.DO_NOTHING)
    assignment_date = models.DateField(blank=True, null=True)
    assignment_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    parking_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    notes = models.TextField(null=True)
    round_trip_distance = models.IntegerField()
    lep_name = models.CharField(max_length=100)
    serviced_name = models.CharField(max_length=100)
    # signature = models.ImageField(upload_to='signatures/', null=True, blank=True)

    def __str__(self):
        return f"{self.interpreter} assigned to {self.job}"

class Timesheet(models.Model):
    assignment = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    interpreter = models.ForeignKey("interpreters.Interpreter", on_delete=models.DO_NOTHING)
    hours_worked = models.DurationField()
    submission_date = models.DateField()
    approval_status = models.BooleanField()