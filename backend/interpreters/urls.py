from django.urls import path
from .views import InterpreterListView, InterpreterSignupView, InterpreterDetailView, InterpreterUpdateView
urlpatterns = [
    path('', InterpreterListView.as_view(), name='interpreter-list'),
    path('signup/', InterpreterSignupView.as_view(), name='signup'),
    path('<int:pk>/', InterpreterDetailView.as_view(), name="interpreter-detail"),
    path('<int:pk>/update/', InterpreterUpdateView.as_view(), name="interpreter-update"),
]