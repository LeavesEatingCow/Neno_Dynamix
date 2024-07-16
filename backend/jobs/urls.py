from django.urls import path
from .views import job_list, job_detail, job_create, JobDetailAPIView
# from .views import api_home

urlpatterns = [
    path('', job_list),
    path('create/', job_create),
    path('<int:pk>/', job_detail),
]