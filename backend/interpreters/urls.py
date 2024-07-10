from django.urls import path
from .views import InterpreterCreateView, InterpreterListCreateAPIView, home_page
# from .views import api_home

urlpatterns = [
    path('', InterpreterListCreateAPIView.as_view()),
    path('hello/', home_page)
]