from django.urls import path
from .views import InterpreterCreateView, InterpreterListCreateAPIView, interpreter_list
# from .views import api_home

urlpatterns = [
    path('', InterpreterListCreateAPIView.as_view()),
    path('all/', interpreter_list)
]