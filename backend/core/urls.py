from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import LandingPageView, CareerPageView, CustomLoginView, UserPasswordUpdateView, profile_redirect_view

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing-page"),
    path("career/", CareerPageView.as_view(), name="career"),
    path('profile/', profile_redirect_view, name="profile-redirect"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('changepassword/', UserPasswordUpdateView.as_view(), name="change-password"),
    path('logout/', LogoutView.as_view(), name="logout"),
]