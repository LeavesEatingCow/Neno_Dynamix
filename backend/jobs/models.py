from django.db import models

# Create your models here.
class Job(models.Model):
    # * job_id (PK)
    # * client_id (FK)
    # * client_job_id (Unique)
    # * job_date
    # * location
    # * practice_name
    # * language
    # * lep_name
    # * expected_duration
    # * description

    client = models.ForeignKey("client.Client", on_delete=models.CASCADE)
    client_job_id = models.CharField(max_length=100, unique=True, null=True)
    job_date = models.DateField()
    location = models.CharField(max_length=100, blank=False)
    practice_name = models.CharField(max_length=100, blank=False)
    language = models.CharField(max_length=100)
    lep_name = models.CharField(max_length=100)
    expected_duration = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return f'{self.client}: {self.location}'