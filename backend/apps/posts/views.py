from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.db import models
from datetime import date


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView

from backend.apps.accounts.models import User
from backend.apps.lessons.models import Subject
from backend.apps.posts.forms import SendMessageForm
from backend.apps.posts.models import Post
from backend.apps.school_info.models import SchoolInfo, Course, Gallery, Service, SocialLink


class IndexView(TemplateView):
    template_name = 'post_list.html'


class PostListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['school_info'] = SchoolInfo.objects.get(id=1)
        context['years'] = date.today().year - context['school_info'].founded.year
        context['teachers'] = User.objects.filter(role=False).count()
        context['students'] = User.objects.filter(role=True).count()
        context['subjects'] = Subject.objects.count()
        context['courses'] = Course.objects.all().order_by('-created')[:3]
        context['galleries'] = Gallery.objects.all().order_by('-created')[:8]
        context['services'] = Service.objects.all().order_by('-created')[:6]
        return context


class AboutUsView(ListView):
    model = User
    template_name = 'about_us.html'
    paginate_by = 2
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(role=False)[:4]
        return context


class CoursesView(ListView):
    model = Course
    template_name = 'courses.html'
    paginate_by = 3
    ordering = ['-created']
    context_object_name = 'courses'


class NewsView(ListView):
    model = Post
    template_name = 'news.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        p = Paginator(Post.objects.all().order_by('-updated'), self.paginate_by)
        context['posts'] = p.page(context['page_obj'].number)
        context['recents'] = Post.objects.all().order_by('-updated')[:5]
        return context


class SendMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

