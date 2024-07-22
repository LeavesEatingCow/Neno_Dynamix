from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import ClientCreationForm

# Create your views here.
class ClientSignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = ClientCreationForm

    def get_success_url(self) -> str:
        return reverse("login")