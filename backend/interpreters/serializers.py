from rest_framework import serializers
from .models import Interpreter

class InterpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpreter
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "address",
            "ssn",
            "username",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

