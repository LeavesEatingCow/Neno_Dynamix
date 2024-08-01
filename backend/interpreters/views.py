from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import Job
from .models import Interpreter, InterpreterApplicant
from .forms import InterpreterProfileForm, InterpreterApplicantForm
# Create your views here.
class InterpreterListView(LoginRequiredMixin, generic.ListView):
    template_name = "interpreters/interpreter_list.html"
    context_object_name = "interpreters"

    def get_queryset(self):
        return Interpreter.objects.all()

class InterpreterSignupView(generic.CreateView):
    template_name = "registration/interpreter_signup.html"
    form_class = InterpreterApplicantForm

    def get_success_url(self) -> str:
        return reverse("core:login")
    
# Go to Profile Page
class InterpreterDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "interpreters/interpreter_detail.html"
    context_object_name = "interpreter"
    def get_object(self):
        interpreter = get_object_or_404(Interpreter, user=self.request.user)
        return interpreter

class InterpreterUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "interpreters/interpreter_update.html"
    form_class = InterpreterProfileForm
    queryset = Interpreter.objects.all()
    
    def get_success_url(self) -> str:
        return reverse("jobs:job-list")
    
class InterpreterJobListView(LoginRequiredMixin, generic.ListView):
    model = Job
    template_name = 'interpreters/interpreter_jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        languages = interpreter.languages.all()
        return Job.objects.filter(language__in=languages)
