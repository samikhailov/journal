from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ArticleCreateForm
from .models import Article, Journal


class JournalListView(ListView):
    model = Journal


class JournalDetailView(DetailView):
    model = Journal


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreate(CreateView):
    form_class = ArticleCreateForm
    model = Article


def blank(request):
    return render(request, 'catalog/for-authors.html')
