import json
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict

from client.mixins import ClientAndLoginRequiredMixin
from client.models import Client
from interpreters.mixins import InterpreterAndLoginRequiredMixin
from interpreters.models import Interpreter
from core.models import Address
from .mixins import ClientIsOwnerMixin
from .models import Job
from .forms import JobForm, JobModelForm
# Create your views here.


class ClientJobListView(ClientAndLoginRequiredMixin, ListView):
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(client=self.request.user.client).order_by('job_date')

class InterpreterJobListView(InterpreterAndLoginRequiredMixin, ListView):
    model = Job
    template_name = "jobs/job_list.html"
    context_object_name = 'jobs'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        languages = interpreter.languages.all()
        return Job.objects.filter(language__in=languages).order_by('-job_date')

class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = "jobs/job_detail.html"
    queryset = Job.objects.all()
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        
        # Create a dictionary to map fields to custom labels
        custom_labels = {
            'client': 'Client Name',
            'client_job_id': 'Job ID',
            'job_date': 'Job Date',
            'job_time': 'Job Time',
            'practice_name': 'Requester\'s Name',
            'language': 'Language',
            'lep_name': 'Patient\'s Name',
            'expected_duration': 'Expected Duration',
            'description': 'Description',
            'status': 'Status',
        }

        # Convert the job object to a dictionary and replace field names with custom labels
        job_dict = {
            custom_labels.get(field, field): str(getattr(job, field))
            for field in custom_labels
        }

        # Add address fields (if job has an associated address)
        if job.address:
            job_dict['Location'] = str(job.address)

        context['job_fields'] = job_dict
        return context

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

# class JobUpdateView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, UpdateView):
#     template_name = "jobs/job_update.html"
#     form_class = JobModelForm
#     queryset = Job.objects.all()

#     def get_success_url(self) -> str:
#         return reverse("jobs:job-list")

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

# class JobDeleteView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, DeleteView):
#     template_name = "jobs/job_delete.html"
#     queryset = Job.objects.all()

#     def get_success_url(self) -> str:
#         return reverse("jobs:job-list")

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
    template_name = 'jobs/job_create.html'

    def form_valid(self, form):
        # Create the Job instance without saving it to the database yet
        job = form.save(commit=False)
        # Assign the client to the current user
        job.client = self.request.user.client
        # Now handle the address fields from the form
        address_data = {
            'street_address': form.cleaned_data['street_address'],
            'apt_number': form.cleaned_data.get('apt_number', ''),
            'city': form.cleaned_data['city'],
            'state': form.cleaned_data['state'],
            'zip_code': form.cleaned_data['zip_code'],
        }

        # Create or update the address instance
        address, _ = Address.objects.get_or_create(
            street_address=address_data['street_address'],
            city=address_data['city'],
            state=address_data['state'],
            zip_code=address_data['zip_code'],
            defaults=address_data
        )

        # Associate the address with the job
        job.address = address
        print(str(job.address))

        # Save the Job instance with the address
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
    template_name = 'jobs/job_create.html'

    def get_object(self, queryset=None):
        job = super().get_object(queryset)
        if job.client != self.request.user.client:
            raise Http404
        return job

    def form_valid(self, form):
        # Save the job object without committing to the database yet
        job = form.save(commit=False)

        # Get the address fields from the form
        address_data = {
            'street_address': form.cleaned_data['street_address'],
            'apt_number': form.cleaned_data.get('apt_number', ''),
            'city': form.cleaned_data['city'],
            'state': form.cleaned_data['state'],
            'zip_code': form.cleaned_data['zip_code'],
        }

        # Check if the job already has an address
        if job.address:
            # Update the existing address with the new form data
            Address.objects.filter(id=job.address.id).update(**address_data)
        else:
            # Create a new address if one does not already exist
            address = Address.objects.create(**address_data)
            job.address = address  # Associate the new address with the job

        # Save the job object to the database
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
    job.status = "CANCELLED"
    job.save()
    if job.status == "OPEN":
        job.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "jobListChanged": None,
                "showMessage": f"{job.client}'s job has been deleted."
            })
        })

class JobDeleteView(ClientAndLoginRequiredMixin, ClientIsOwnerMixin, DeleteView):
    model = Job
    template_name = "jobs/job_list.html"
    
    def get_success_url(self):
        return reverse('jobs:client-job-list')
    
    def form_valid(self, form):
        job = self.get_object()

        # Check the job's status
        if job.status == 'OPEN':
            # If status is 'OPEN', proceed with deletion
            return super().form_valid(form)
        else:
            # If status is not 'OPEN', change to 'CANCELLED'
            job.status = 'CANCELLED'
            job.save()
            return HttpResponseRedirect(self.get_success_url())