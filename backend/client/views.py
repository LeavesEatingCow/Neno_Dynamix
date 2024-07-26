from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Client
from .forms import ClientCreationForm, ClientProfileForm

# Create your views here.
class ClientSignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = ClientCreationForm

    def get_success_url(self) -> str:
        return reverse("login")
    
# Go to Profile Page
class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "client/client_detail.html"
    context_object_name = "client"
    def get_object(self):
        client = get_object_or_404(Client, user=self.request.user)
        return client
    

class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "client/client_update.html"
    form_class = ClientProfileForm
    queryset = Client.objects.all()
    
    def get_success_url(self) -> str:
        return reverse("jobs:job-list")