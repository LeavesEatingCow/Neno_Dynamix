from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Interpreter
from .forms import InterpreterCreationForm
# Create your views here.
class InterpreterListView(LoginRequiredMixin, generic.ListView):
    template_name = "interpreters/interpreter_list.html"
    context_object_name = "interpreters"

    def get_queryset(self):
        return Interpreter.objects.all()

class InterpreterSignupView(generic.CreateView):
    template_name = "registration/interpreter_signup.html"
    form_class = InterpreterCreationForm

    def get_success_url(self) -> str:
        return reverse("login")