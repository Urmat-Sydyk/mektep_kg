from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import models


# Create your views here.
from django.views.generic import ListView

from backend.apps.posts.models import Post


def index(request):
    print(request)
    return HttpResponse("Main")


class PostListView(ListView):
    models = Post
    paginate_by = 10
    template_name ='post_list.html'
