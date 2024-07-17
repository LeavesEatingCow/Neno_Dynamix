from django.urls import path
from .views import job_list, job_detail, job_create, job_update, job_delete, JobDetailAPIView
# from .views import api_home

urlpatterns = [
    path('', job_list, name='job-list'),
    path('<int:pk>/', job_detail, name="job-detail"),
    path('create/', job_create, name="job-create"),
    path('<int:pk>/update/', job_update, name="job-update"),
    path('<int:pk>/delete/', job_delete, name="job-delete"),
]