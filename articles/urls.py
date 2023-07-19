from django.contrib import admin
from django.urls import include, path
from articles.views import List, Detail

app_name = "articles"

urlpatterns = [
    path("", List.as_view(), name="list"),
    path("<int:pk>/", Detail.as_view(), name="detail"),
]
