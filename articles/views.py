from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from articles.models import Article
from articles.forms import NewArticleForm


class List(ListView):
    """전체 리스트를 보여주기"""

    template_name = "list.html"
    model = Article
    queryset = Article.objects.all().order_by("-modified_at")
    paginate_by = 0


class Detail(DetailView):
    """상세 페이지"""

    template_name = "view.html"
    model = Article

class New(CreateView):
    """Create new article"""

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """get template and context to draw page"""
        form = NewArticleForm()
        context = {"form": form}

        return render(
            request,
            "write.html",
            context=context,
        )

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """post request that creates a new article"""
        # TODO impl
        return super().post(request, *args, **kwargs)
