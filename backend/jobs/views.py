from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm, JobModelForm
from client.models import Client

from rest_framework import generics
from .serializers import JobSerializer

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()

    context = {
        "jobs": jobs
    }

    return render(request, "jobs/job_list.html", context)

def job_detail(request, pk):
    job = Job.objects.get(id=pk)

    context = {
        "job": job
    }

    return render(request, "jobs/job_detail.html", context)

def job_create(request):
    form = JobModelForm()
    if request.method == "POST":
        form = JobModelForm(request.POST) # To keep data on screen

        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)

            job_id = form.cleaned_data['job_id']
            job_date = form.cleaned_data['job_date']
            location = form.cleaned_data['location']
            practice_name = form.cleaned_data['practice_name']
            language = form.cleaned_data['language']
            lep_name = form.cleaned_data['lep_name']
            expected_duration = form.cleaned_data['expected_duration']
            description = form.cleaned_data['description']
            client = form.cleaned_data['client']

            Job.objects.create(
                client_job_id=job_id,
                job_date=job_date,
                location=location,
                practice_name=practice_name,
                language=language,
                lep_name=lep_name,
                expected_duration=expected_duration,
                description=description,
                client=client,
            )
            print("Job Created")
            return redirect("/api/jobs/")

        else:
            print("Invalid Form")
        

    context = {
        "form": form
    }
    return render(request, "jobs/job_create.html", context)

# def job_create(request):
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

#             Job.objects.create(
#                 client_job_id=job_id,
#                 job_date=job_date,
#                 location=location,
#                 practice_name=practice_name,
#                 language=language,
#                 lep_name=lep_name,
#                 expected_duration=expected_duration,
#                 description=description,
#                 client=client,
#             )
#             print("Job Created")
#             return redirect("/api/jobs/")

#         else:
#             print("Invalid Form")
        

#     context = {
#         "form": form
#     }
#     return render(request, "jobs/job_create.html", context)

class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer