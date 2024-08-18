from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from client.mixins import ClientAndLoginRequiredMixin
from client.models import Client
from .mixins import ClientIsOwnerMixin
from .models import Job
from .forms import JobForm, JobModelForm
# Create your views here.

class JobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    queryset = Job.objects.all()
    context_object_name = "jobs"

class ClientJobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "client/client_job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(client=self.request.user.client)

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

class JobCreateView(ClientAndLoginRequiredMixin, CreateView):
    template_name = "jobs/job_create.html"
    form_class = JobModelForm

    def get_success_url(self) -> str:
        return reverse("jobs:job-list")
    
    def form_valid(self, form):
        form.instance.client = self.request.user.client
        return super().form_valid(form)
        

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

# def job_update(request, pk):
#     job = Job.objects.get(id=pk)
#     form = JobForm()
#     if request.method == "POST":
#         form = JobForm(request.POST) # To keep data on screen

#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)

#             job_id = form.cleaned_data['job_id']
#             job_date = form.cleaned_data['job_date']
#             location = form.cleaned_data['location']
#             practice_name = form.cleaned_data['practice_name']
#             language = form.cleaned_data['language']
#             lep_name = form.cleaned_data['lep_name']
#             expected_duration = form.cleaned_data['expected_duration']
#             description = form.cleaned_data['description']
#             client = Client.objects.first()

#             job.client_job_id = job_id
#             job.job_date = job_date 
#             job.location = location
#             job.practice_name = practice_name
#             job.language = language
#             job.lep_name = lep_name
#             job.expected_duration = expected_duration
#             job.description = description
#             job.client = client
#             # Commit save
#             job.save()
#             print("Job Created")
#             return redirect("/api/jobs/")

#         else:
#             print("Invalid Form")
        

#     context = {
#         "form": form,
#         "job": job,
#     }

#     return render(request, "jobs/job_update.html", context)


# def job_create(request):
    # form = JobForm()
    # if request.method == "POST":
    #     form = JobForm(request.POST) # To keep data on screen

    #     if form.is_valid():
    #         print("The form is valid")
    #         print(form.cleaned_data)

    #         job_id = form.cleaned_data['job_id']
    #         job_date = form.cleaned_data['job_date']
    #         location = form.cleaned_data['location']
    #         practice_name = form.cleaned_data['practice_name']
    #         language = form.cleaned_data['language']
    #         lep_name = form.cleaned_data['lep_name']
    #         expected_duration = form.cleaned_data['expected_duration']
    #         description = form.cleaned_data['description']
    #         client = Client.objects.first()

    #         Job.objects.create(
    #             client_job_id=job_id,
    #             job_date=job_date,
    #             location=location,
    #             practice_name=practice_name,
    #             language=language,
    #             lep_name=lep_name,
    #             expected_duration=expected_duration,
    #             description=description,
    #             client=client,
    #         )
    #         print("Job Created")
    #         return redirect("/api/jobs/")

    #     else:
    #         print("Invalid Form")
        

    # context = {
    #     "form": form
    # }
#     return render(request, "jobs/job_create.html", context)

