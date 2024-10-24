from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Assignment, Timesheet
from .forms import AssignmentUpdateForm
from jobs.models import Job
from core.models import Address
# Create your views here.


    
def create_assignment(request, *args, **kwargs):
    job_id = kwargs.get('pk')
    job = get_object_or_404(Job, pk=job_id)
    interpreter = request.user.interpreter  # Assuming the user is an interpreter

    # Check if the job has already been assigned
    if hasattr(job, 'assignment'):
        messages.error(request, 'This job has already been accepted by another interpreter.')
        return redirect('jobs:interpreter-job-list')
    
    # Create an assignment
    assignment = Assignment.objects.create(
        interpreter=interpreter,
        job=job,
        assignment_date=job.job_date,
        assignment_time=job.job_time,
        location=job.address,
        language=job.language.name,
        lep_name=job.lep_name,
        serviced_name=job.practice_name,
    )

    # Update the job status
    job.status = 'IN_PROGRESS'
    job.save()

    messages.success(request, 'You have successfully accepted the job.')
    # return redirect('assignments:assignment_detail', pk=assignment.pk)
    return redirect('assignments:view-assignment', pk=assignment.pk)
    

class ActiveAssignmentListView(ListView):
    model = Assignment
    template_name = "assignments/assignment_list.html"
    context_object_name = 'assignments'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        return Assignment.objects.filter(
            interpreter=interpreter,
            job__status="IN_PROGRESS"
            )

class CompletedAssignmentListView(ListView):
    model = Assignment
    template_name = "assignments/assignment_list.html"
    context_object_name = 'assignments'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        return Assignment.objects.filter(
            interpreter=interpreter,
            job__status="COMPLETED"
            )

class AssignmentUpdateView(UpdateView):
    template_name = "assignments/assignment_detail.html"
    queryset = Assignment.objects.all()
    form_class = AssignmentUpdateForm
    context_object_name = "assignment"

    def get_success_url(self):
        return reverse_lazy('assignments:view-assignment', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        # Check if the "Save" or "Submit" button was pressed
        if 'save_assignment' in self.request.POST:
            # Allow saving even if some required fields are not filled
            assignment = form.save(commit=False)
            assignment.save()
            messages.success(self.request, 'Assignment saved successfully.')
            return redirect('assignments:view-assignment', pk=assignment.pk)

        elif 'submit_assignment' in self.request.POST:
            # Perform full validation for submission
            if form.is_valid():
                assignment = form.save(commit=False)
                # Ensure all required fields are filled
                required_fields = ['arrival_time', 'start_time', 'end_time']
                missing_fields = [field for field in required_fields if not getattr(assignment, field)]

                if missing_fields:
                    messages.error(self.request, 'Please fill in all required fields before submitting.')
                    return self.form_invalid(form)
                
                assignment.job.status = "COMPLETED"
                assignment.job.save()
                assignment.save()
                
                messages.success(self.request, 'Assignment submitted successfully.')
                return redirect('assignments:view-assignment', pk=assignment.pk)
            else:
                return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your submission.')
        return super().form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     assignment = self.get_object()
        
    #     # Create a dictionary to map fields to custom labels
    #     custom_labels = {
    #         'interpreter' : 'Interpreter',
    #         'job' : 'Job',
    #         'assignment_date' : 'Date',
    #         'assignment_time' : 'Time',
    #         'location' : 'Location',
    #         'language' : 'Language',
    #         'arrival_time' : 'Arrival Time',
    #         'start_time' : 'Start Time',
    #         'end_time' : 'End Time',
    #         'parking_fee' : 'Parking Fee',
    #         'notes' : 'Additional Notes',
    #         'round_trip_distance' : 'Round Trip Distance',
    #         'lep_name' : 'Limited English Person',
    #         'serviced_name' : 'Requester\'s Name',
    #     }

    #     # Convert the assignment object to a dictionary and replace field names with custom labels
    #     assignment_dict = {
    #         custom_labels.get(field, field): str(getattr(assignment, field))
    #         for field in custom_labels
    #     }

    #     context['assignment_fields'] = assignment_dict
    #     return context