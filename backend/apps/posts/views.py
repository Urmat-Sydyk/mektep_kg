from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.db import models


# Create your views here.
from django.views.generic import ListView, TemplateView

from backend.apps.posts.models import Post


class IndexView(TemplateView):
    template_name = 'post_list.html'


class PostListView(ListView):
    model = Post
    paginate_by = 4
    template_name ='post_list.html'
    context_object_name = 'posts'
