from django.urls import path
from articles.views import List, Detail, New

app_name = "articles"

urlpatterns = [
    path("", List.as_view(), name="list"),
    path("<int:pk>/", Detail.as_view(), name="detail"),
    path("write/", New.as_view(), name="new"),
]
