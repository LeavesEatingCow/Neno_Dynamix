from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Assignment
from jobs.models import Job
# Create your views here.

class AssignmentCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        job_id = kwargs.get('pk')
        job = get_object_or_404(Job, pk=job_id)
        interpreter = request.user.interpreter  # Assuming the user is an interpreter

        # Check if the job has already been assigned
        if hasattr(job, 'assignment'):
            messages.error(request, 'This job has already been accepted by another interpreter.')
            return redirect('jobs:view-job', pk=job_id)

        # Create an assignment
        assignment = Assignment.objects.create(
            interpreter=interpreter,
            job=job,
            assignment_date=job.job_date,
            assignment_time=job.job_time,
            location=job.location,
            language=job.language.name,
            lep_name=job.lep_name,
            serviced_name=job.practice_name,
        )

        # Update the job status
        job.status = 'IN_PROGRESS'
        job.save()

        messages.success(request, 'You have successfully accepted the job.')
        # return redirect('assignments:assignment_detail', pk=assignment.pk)
        return redirect('jobs:job_detail', pk=job_id)
    

class ActiveAssignmentListView(ListView):
    model = Assignment
    template_name = "assignments/assignment_list.html"
    context_object_name = 'assignments'

    def get_queryset(self):
        interpreter = self.request.user.interpreter
        # print(Assignment.objects.filter(interpreter=interpreter))
        return Assignment.objects.filter(interpreter=interpreter)

class AssignmentDetailView(DetailView):
    template_name = "assignments/assignment_detail.html"
    queryset = Assignment.objects.all()
    context_object_name = "assignment"