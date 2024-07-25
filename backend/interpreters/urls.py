from django.urls import path
from .views import InterpreterListView, InterpreterSignupView
urlpatterns = [
    path('', InterpreterListView.as_view(), name='interpreters'),
    path('signup/', InterpreterSignupView.as_view(), name='signup')
]