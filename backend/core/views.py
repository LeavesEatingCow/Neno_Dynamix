from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse("login")
    
# def home_page(request):
#     return render(request, "landing_page.html")