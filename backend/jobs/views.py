from typing import Any
import json
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from client.mixins import ClientAndLoginRequiredMixin
from client.models import Client
from interpreters.mixins import InterpreterAndLoginRequiredMixin
from interpreters.models import Interpreter
from .mixins import ClientIsOwnerMixin
from .models import Job
from .forms import JobForm, JobModelForm
# Create your views here.

class JobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    queryset = Job.objects.all()
    context_object_name = "jobs"

class ClientJobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(client=self.request.user.client).order_by('-id')

class InterpreterJobListView(InterpreterAndLoginRequiredMixin, ListView):
    model = Job
    template_name = 'interpreters/interpreter_job_list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        languages = interpreter.languages.all()
        return Job.objects.filter(language__in=languages)

def job_list(request):
    jobs = Job.objects.all()

    context = {
        "jobs": jobs
    }

    return render(request, "jobs/job_list.html", context)

class JobDetailView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, DeleteView):
    template_name = "jobs/job_detail.html"
    queryset = Job.objects.all()
    context_object_name = "job"

def job_detail(request, pk):
    job = Job.objects.get(id=pk)

    context = {
        "job": job
    }

    return render(request, "jobs/job_detail.html", context)

# class JobCreateView(ClientAndLoginRequiredMixin, CreateView):
#     template_name = "jobs/job_create.html"
#     form_class = JobModelForm

#     def get_success_url(self) -> str:
#         return reverse("jobs:job-list")
    
#     def form_valid(self, form):
#         form.instance.client = self.request.user.client
#         return super().form_valid(form)
        

def job_create(request):
    form = JobModelForm()
    if request.method == "POST":
        form = JobModelForm(request.POST) # To keep data on screen

        if form.is_valid():
            form.save()
            return redirect("/jobs/")

        else:
            print("Invalid Form")
        

    context = {
        "form": form
    }
    return render(request, "jobs/job_create.html", context)

class JobUpdateView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, UpdateView):
    template_name = "jobs/job_update.html"
    form_class = JobModelForm
    queryset = Job.objects.all()

    def get_success_url(self) -> str:
        return reverse("jobs:job-list")

def job_update(request, pk):
    job = Job.objects.get(id=pk)
    form = JobModelForm(instance=job)
    if request.method == "POST":
        form = JobModelForm(request.POST, instance=job) # To keep data on screen

        if form.is_valid():
            form.save()
            return redirect("/jobs/")

        else:
            print("Invalid Form")
        

    context = {
        "form": form,
        "job": job,
    }

    return render(request, "jobs/job_update.html", context)

class JobDeleteView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, DeleteView):
    template_name = "jobs/job_delete.html"
    queryset = Job.objects.all()

    def get_success_url(self) -> str:
        return reverse("jobs:job-list")

def job_delete(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect("/jobs/")

# Create your views here.
def index(request):
    return render(request, 'client/client_job_list.html', {})

class JobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    queryset = Job.objects.all()
    context_object_name = "jobs"

class JobCreateView(ClientAndLoginRequiredMixin, CreateView):
    model = Job
    form_class = JobModelForm
    template_name = 'jobs/job_form.html'

    def form_valid(self, form):
        # Create the Job instance without saving it to the database yet
        job = form.save(commit=False)
        # Assign the client to the current user
        job.client = self.request.user.client
        # Save the Job instance to the database
        job.save()

        # Returning a response with HTMX trigger headers
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "jobListChanged": None,
                    "showMessage": f"{job.client}'s job has been added."
                })
            }
        )
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

def add_job(request):
    if request.method == "POST":
        form = JobModelForm(request.POST)
        if form.is_valid():
            job = Job.objects.create(
                client = request.user.client,
                client_job_id = form.cleaned_data.get('client_job_id'),
                job_date = form.cleaned_data.get('job_date'),
                location = form.cleaned_data.get('location'),
                practice_name = form.cleaned_data.get('practice_name'),
                language = form.cleaned_data.get('language'),
                lep_name = form.cleaned_data.get('lep_name'),
                expected_duration = form.cleaned_data.get('expected_duration'),
                description = form.cleaned_data.get('description'),
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "jobListChanged": None,
                        "showMessage": f"{job.client}'s job has been added."
                    })
                })
        else:
            return render(request, 'jobs/job_form.html', {
                'form': form,
            })
    else:
        form = JobModelForm()
    return render(request, 'jobs/job_form.html', {
        'form': form,
    })

class JobUpdateView(ClientAndLoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobModelForm
    template_name = 'jobs/job_form.html'

    def get_object(self, queryset=None):
        job = super().get_object(queryset)
        if job.client != self.request.user.client:
            raise Http404
        return job

    def form_valid(self, form):
        job = form.save()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "jobListChanged": None,
                    "showMessage": f"{job.client}'s job has been updated."
                })
            }
        )

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.client != request.user.client:
        raise Http404
    if request.method == "POST":
        form = JobModelForm(request.POST, instance=job)

        if form.is_valid():
            job.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "jobListChanged": None,
                        "showMessage": f"{job.client}'s job has been updated."
                    })
                }
            )
        else:
            print(form.errors)
            return render(request, 'jobs/job_form.html', {
                'form': form,
                'job': job,
            })
    else:
        form = JobModelForm(instance=job)
    return render(request, 'jobs/job_form.html', {
        'form': form,
        'job': job,
    })

def remove_job_confirmation(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.client != request.user.client:
        raise Http404
    return render(request, 'jobs/job_delete_confirmation.html', {
        'job': job,
    })

@ require_POST
def remove_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.client != request.user.client:
        raise Http404
    job.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "jobListChanged": None,
                "showMessage": f"{job.client}'s job has been deleted."
            })
        })