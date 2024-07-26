from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"


@login_required
def profile_redirect_view(request):
    user = request.user
    if user.is_client:
        return redirect('clients:client-detail', pk=user.client.pk)
    elif user.is_interpreter:
        return redirect('interpreters:interpreter-detail', pk=user.interpreter.pk)
    else:
        return redirect('/')
