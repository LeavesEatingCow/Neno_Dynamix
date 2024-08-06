from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from jobs.models import Job
from core.mixins import UserIsOwnerMixin
from .models import Interpreter, InterpreterApplicant
from .forms import InterpreterProfileForm, InterpreterApplicantForm
from .mixins import InterpreterAndLoginRequiredMixin
# Create your views here.
class InterpreterListView(LoginRequiredMixin, generic.ListView):
    template_name = "interpreters/interpreter_list.html"
    context_object_name = "interpreters"

    def get_queryset(self):
        return Interpreter.objects.all()
    

class InterpreterSignupView(generic.CreateView):
    template_name = "registration/interpreter_signup.html"
    form_class = InterpreterApplicantForm

    # def form_valid(self, form):
    #     application = form.save()
    #     uploaded_file = self.request.FILES['resume']
    #     fs = FileSystemStorage()
    #     fs.save(uploaded_file.name, uploaded_file)
    #     return super().form_valid(form)
    

    def get_success_url(self) -> str:
        return reverse("core:login")
 
    
# Go to Profile Page
class InterpreterDetailView(InterpreterAndLoginRequiredMixin, UserIsOwnerMixin, generic.DetailView):
    template_name = "interpreters/interpreter_detail.html"
    context_object_name = "interpreter"
    queryset = Interpreter.objects.all()
class InterpreterUpdateView(InterpreterAndLoginRequiredMixin, UserIsOwnerMixin, generic.UpdateView):
    template_name = "interpreters/interpreter_update.html"
    form_class = InterpreterProfileForm
    queryset = Interpreter.objects.all()
    
    def get_success_url(self) -> str:
        return reverse("jobs:job-list")
    
class InterpreterJobListView(InterpreterAndLoginRequiredMixin, generic.ListView):
    model = Job
    template_name = 'interpreters/interpreter_jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        languages = interpreter.languages.all()
        return Job.objects.filter(language__in=languages)
