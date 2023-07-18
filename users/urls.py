from django.urls import path
from users.views import SigninView, SignupView, SignoutView

app_name = "users"

urlpatterns = [
    path("signin/", SigninView.as_view(), name="signin"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("signout/", SignoutView.as_view(), name="signout"),
]
