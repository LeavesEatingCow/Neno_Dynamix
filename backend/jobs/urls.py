from django.urls import path
from .views import ClientJobListView
from . import views

# from .views import (job_list, job_detail, job_create, job_update, job_delete,
#                      JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView)
# # from .views import api_home

# urlpatterns = [
#     path('', JobListView.as_view(), name='job-list'),
#     path('<int:pk>/', JobDetailView.as_view(), name="job-detail"),
#     path('create/', JobCreateView.as_view(), name="job-create"),
#     path('<int:pk>/update/', JobUpdateView.as_view(), name="job-update"),
#     path('<int:pk>/delete/', JobDeleteView.as_view(), name="job-delete"),
# ]

urlpatterns = [
    path('jobs', ClientJobListView.as_view(), name='job-list'),
    path('jobs/add', views.add_job, name='add-job'),
    path('jobs/<int:pk>/remove_confirmation', views.remove_job_confirmation, name='remove-job-confirmation'),
    path('jobs/<int:pk>/remove', views.remove_job, name='remove-job'),
    path('jobs/<int:pk>/edit', views.edit_job, name='edit-job'),
]