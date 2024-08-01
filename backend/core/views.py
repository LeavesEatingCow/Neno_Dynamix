from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from .models import User

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

class CareerPageView(TemplateView):
    template_name = "career.html"

class UserPasswordUpdateView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"    

    def form_valid(self, form):
        self.request.user.password_changed = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:landing-page")

class CustomLoginView(LoginView):
    next_page = None
    
    def get_success_url(self):
        user = self.request.user
        if not user.password_changed:
            self.next_page = reverse_lazy("core:change-password")
        return self.get_redirect_url() or self.get_default_redirect_url()
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)

@login_required
def profile_redirect_view(request):
    user = request.user
    if user.is_client:
        return redirect('clients:client-detail', pk=user.client.pk)
    elif user.is_interpreter:
        return redirect('interpreters:interpreter-detail', pk=user.interpreter.pk)
    else:
        return redirect('/')
