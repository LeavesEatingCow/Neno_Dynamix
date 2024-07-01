from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    pass