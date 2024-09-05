from django.urls import path
from .views import (
    InterpreterListView, InterpreterSignupView, InterpreterDetailView, 
    InterpreterUpdateView, InterpreterDashboardView, InterpreterAssignmentView,
    InterpreterCompletedAssignmentView
    )
urlpatterns = [
    path('', InterpreterListView.as_view(), name='interpreter-list'),
    path('signup/', InterpreterSignupView.as_view(), name='signup'),
    path('<int:pk>/', InterpreterDetailView.as_view(), name="interpreter-detail"),
    path('<int:pk>/update/', InterpreterUpdateView.as_view(), name="interpreter-update"),
    path('dashboard/', InterpreterDashboardView.as_view(), name='interpreter-dashboard'),
    path('assignments/', InterpreterAssignmentView.as_view(), name='interpreter-assignments'),
    path('assignments/completed', InterpreterCompletedAssignmentView.as_view(), name='interpreter-completed-assignments'),
]