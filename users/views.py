from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import User


class SigninView(LoginView):
    template_name = "login.html"


class SignoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"


class SignupView(CreateView):
    template_name = "join.html"
    model = User
    fields = "__all__"
