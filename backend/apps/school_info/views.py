from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from backend.apps.school_info.models import *
# Create your views here.


class SchoolInfoView(ListView):
    template_name = 'school_info_main.html'
    model = SchoolInfo
    context_object_name = 'info'


