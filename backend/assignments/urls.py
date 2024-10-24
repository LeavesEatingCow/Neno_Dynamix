from django.urls import path
from .views import (
    create_assignment, ActiveAssignmentListView, AssignmentUpdateView, CompletedAssignmentListView
)

urlpatterns = [
    path('', ActiveAssignmentListView.as_view(), name='assignment-list'),
    path('completed/', CompletedAssignmentListView.as_view(), name='completed-assignments'),
    path('<int:pk>/', AssignmentUpdateView.as_view(), name='view-assignment'),
    path('<int:pk>/add/', create_assignment, name='add-assignment'),
]