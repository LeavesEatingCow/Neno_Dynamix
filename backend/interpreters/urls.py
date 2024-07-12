from django.urls import path
from .views import InterpreterCreateView, InterpreterListCreateAPIView
# from .views import api_home

urlpatterns = [
    path('', InterpreterListCreateAPIView.as_view()),
]