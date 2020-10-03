from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.

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