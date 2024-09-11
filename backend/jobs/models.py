from django.db import models
from datetime import datetime

# Create your models here.
class Job(models.Model):
    status_choices = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    client_job_id = models.CharField(max_length=100, unique=True, null=True)
    job_date = models.DateField()
    job_time = models.TimeField()
    date_posted = models.DateTimeField(default=datetime.now)
    address = models.ForeignKey("core.Address", on_delete=models.SET_NULL, null=True)
    practice_name = models.CharField(max_length=255)
    language = models.ForeignKey("interpreters.Language", on_delete=models.DO_NOTHING)
    lep_name = models.CharField(max_length=50)
    expected_duration = models.DurationField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default='OPEN')

    def __str__(self):
        return f'{self.client}: {self.language}'