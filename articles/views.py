from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from articles.models import Article
from articles.forms import ArticleForm


class List(ListView):
    """전체 리스트를 보여주기"""

    template_name = "list.html"
    model = Article
    queryset = Article.objects.all().order_by("-modified_at")
    paginate_by = 2


class Detail(DetailView):
    """상세 페이지"""

    template_name = "view.html"
    model = Article


class New(LoginRequiredMixin, CreateView):
    """Create new article"""

    model = Article
    template_name = "write.html"
    form_class = ArticleForm
    success_url = reverse_lazy("articles:list")
    queryset = model.objects.all()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """form.is_valid()가 통과하면 무조건 실행되는 메서드, save 하기 전에
        여기에 `author` 정보를 추가해야 한다."""
        form.instance.author = self.request.user

        return super().form_valid(form)


class Modify(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """글 수정"""

    model = Article
    template_name = "update.html"
    form_class = ArticleForm
    success_url = reverse_lazy("articles:list")
    queryset = model.objects.all()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """form.is_valid()가 통과하면 무조건 실행되는 메서드, save 하기 전에
        여기에 `author` 정보를 추가해야 한다."""
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self) -> bool | None:
        """author와 request 유저와 일치하여야 함."""
        # TODO - impl
        return True


class Remove(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """글 삭제 확인페이지.
    문서에 따르면 요청 메서드가 POST일 경우에만 삭제를 수행한다고 하니 참고바람."""

    model = Article
    template_name = "delete.html"
    success_url = reverse_lazy("articles:list")
    queryset = model.objects.all()

    def test_func(self) -> bool | None:
        """author와 request 유저와 일치하여야 함."""
        # TODO - impl
        return True
