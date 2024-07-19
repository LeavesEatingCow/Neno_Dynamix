from django.urls import path
from .views import (job_list, job_detail, job_create, job_update, job_delete,
                     JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView)
# from .views import api_home

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name="job-detail"),
    path('create/', JobCreateView.as_view(), name="job-create"),
    path('<int:pk>/update/', JobUpdateView.as_view(), name="job-update"),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name="job-delete"),
]