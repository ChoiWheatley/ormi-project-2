from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class New(LoginRequiredMixin, CreateView):
    """Create new article"""
    template_name = "write.html"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """get template and context to draw page"""
        form = NewArticleForm()
        context = {"form": form}

        return render(
            request,
            self.template_name,
            context=context,
        )

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """post request that creates a new article"""
        form = NewArticleForm(request.POST)
        if form.is_valid():
            # save and redirect

            article = form.save(commit=False)
            article.author = request.user
            article.save()

            return redirect(reverse_lazy("articles:list"))

        return render(request, self.template_name, context={"form": form})
