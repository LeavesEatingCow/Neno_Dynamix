from django.shortcuts import render

from rest_framework import generics
from .serializers import InterpreterSerializer
from .models import Interpreter

# Create your views here.
class InterpreterCreateView(generics.CreateAPIView):
    queryset = Interpreter.objects.all()
    serializer_class = InterpreterSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    


class InterpreterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Interpreter.objects.all()
    serializer_class = InterpreterSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)