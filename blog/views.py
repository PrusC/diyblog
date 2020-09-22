from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.

def index(request):
    return render(request, 'index.html', context={})


class BloggerDetailView(generic.DetailView):
    model = models.Blogger