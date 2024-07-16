from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "client",
            "client_job_id",
            "location",
            'practice_name',
            'language',
            'lep_name',
            'expected_duration',
            'description',
        ]