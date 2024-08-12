from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from core.mixins import UserIsOwnerMixin
from .models import Client
from .forms import ClientApplicantForm, ClientProfileForm
from .mixins import ClientAndLoginRequiredMixin
# Create your views here.
class ClientSignupView(CreateView):
    template_name = "client/client_signup.html"
    form_class = ClientApplicantForm

    def get_success_url(self) -> str:
        return reverse("core:login")
    
# Go to Profile Page
class ClientDetailView(ClientAndLoginRequiredMixin, UserIsOwnerMixin, generic.DetailView):
    template_name = "client/client_detail.html"
    context_object_name = "client"
    queryset = Client.objects.all()

class ClientUpdateView(ClientAndLoginRequiredMixin, UserIsOwnerMixin, generic.UpdateView):
    template_name = "client/client_update.html"
    form_class = ClientProfileForm
    queryset = Client.objects.all()
    
    def get_success_url(self) -> str:
        return reverse("jobs:job-list")