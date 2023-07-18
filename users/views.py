from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class SigninView(LoginView):
    template_name = "login.html"


class SignoutView(LogoutView):
    template_name = "logout.html"


class SignupView(CreateView):
    pass
