from django.urls import path
from .views import ClientSignupView, ClientDetailView, ClientUpdateView, ClientDashboardView

urlpatterns = [
    path('signup/', ClientSignupView.as_view(), name="signup"),
    path('<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name="client-update"),
    path('dashboard/', ClientDashboardView.as_view(), name="client-dashbaord")
]