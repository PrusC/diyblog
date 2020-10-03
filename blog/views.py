from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from . import models


def index(request):
    return render(request, 'index.html', context={})


class BloggerDetailView(generic.DetailView):
    model = models.Blogger


class PostDetailView(generic.DetailView):
    model = models.Post


class PostListView(generic.ListView):
    model = models.Post
    paginate_by = 10


class BloggerListView(generic.ListView):
    model = models.Blogger
    paginate_by = 10


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ['text',]

    def get_success_url(self):
        return reverse()
