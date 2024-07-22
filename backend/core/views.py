from django.shortcuts import render, reverse
from django.views.generic import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

    
# def home_page(request):
#     return render(request, "landing_page.html")