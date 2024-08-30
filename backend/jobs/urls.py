from django.urls import path
from .views import (
    ClientJobListView, InterpreterJobListView, JobCreateView, JobUpdateView, JobDetailView,
    remove_job, remove_job_confirmation
)

urlpatterns = [
    path('client/', ClientJobListView.as_view(), name='client-job-list'),
    path('interpreter/', InterpreterJobListView.as_view(), name='interpreter-job-list'),
    path('add/', JobCreateView.as_view(), name='add-job'),
    path('<int:pk>/', JobDetailView.as_view(), name='view-job'),
    path('<int:pk>/edit/', JobUpdateView.as_view(), name='edit-job'),
    path('<int:pk>/remove_confirmation/', remove_job_confirmation, name='remove-job-confirmation'),
    path('<int:pk>/remove/', remove_job, name='remove-job'),
]