from typing import Any, Optional
from urllib import request
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from articles.models import Article
from articles.forms import ArticleForm


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
        form = ArticleForm()
        context = {"form": form}

        return render(
            request,
            self.template_name,
            context=context,
        )

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """post request that creates a new article"""
        form = ArticleForm(request.POST)
        if form.is_valid():
            # save and redirect

            article = form.save(commit=False)
            article.author = request.user
            article.save()

            return redirect(reverse("articles:list"))

        return render(request, self.template_name, context={"form": form})


class Modify(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """글 수정"""

    model = Article
    template_name = "update.html"
    form_class = ArticleForm
    success_url = reverse_lazy("articles:list")
    queryset = model.objects.all()

    # def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    #     """post request that updates a article"""
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(self.success_url)
    #     return HttpResponseForbidden()

    def test_func(self) -> bool | None:
        """author와 request 유저와 일치하여야 함."""
        # TODO - impl
        return True
