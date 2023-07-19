from django.views.generic import ListView, DetailView
from articles.models import Article


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO like user, visit count
        return context
