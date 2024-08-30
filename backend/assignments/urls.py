from django.urls import path
from .views import (
    AssignmentCreateView, ActiveAssignmentListView, AssignmentDetailView
)

urlpatterns = [
    path('', ActiveAssignmentListView.as_view(), name='assignment-list'),
    path('<int:pk>/', AssignmentDetailView.as_view(), name='view-assignment'),
    path('<int:pk>/add/', AssignmentCreateView.as_view(), name='add-assignment'),
]