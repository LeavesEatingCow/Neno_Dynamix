from django.urls import path
from .views import ClientSignupView, ClientDetailView, ClientUpdateView
from jobs.views import ClientJobListView

urlpatterns = [
    path('signup/', ClientSignupView.as_view(), name="signup"),
    path('<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name="client-update"),
    path('dashboard/', ClientJobListView.as_view(), name="client-dashbaord")
]