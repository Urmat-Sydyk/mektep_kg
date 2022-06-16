from django.shortcuts import render

# Create your views here.
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponse


# Create your views here.
from django.views.generic import ListView

from backend.apps.lessons.models import *


def index(request):
    print(request)
    return HttpResponse("Lessons")


class StudentTimeTableView(ListView):
    model = TimeTable
    template_name = 'student_time_table.html'
    context_object_name = 'time_tables'

    def get_queryset(self):
        queryset = TimeTable.objects.filter(student_group=self.request.user.student.student_group).order_by('lesson')
        return queryset


class StudentGradeTableView(ListView):
    model = Grade
    template_name = 'student_grade_table.html'
    context_object_name = 'grades'

    def get_queryset(self):
        queryset = Grade.objects.filter(student=self.request.user.id).order_by('grade_date')
        return queryset
