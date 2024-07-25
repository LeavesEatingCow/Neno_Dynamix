from django.urls import path
from .views import ClientSignupView

urlpatterns = [
    path('signup/', ClientSignupView.as_view(), name="signup")
]