from django.urls import path
from .views import (
    AssignmentCreateView, ActiveAssignmentListView, AssignmentUpdateView, CompletedAssignmentListView
)

urlpatterns = [
    path('', ActiveAssignmentListView.as_view(), name='assignment-list'),
    path('completed/', CompletedAssignmentListView.as_view(), name='completed-assignments'),
    path('<int:pk>/', AssignmentUpdateView.as_view(), name='view-assignment'),
    path('<int:pk>/add/', AssignmentCreateView.as_view(), name='add-assignment'),
]