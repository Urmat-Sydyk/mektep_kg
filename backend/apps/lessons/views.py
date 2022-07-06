from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from backend.apps.lessons.forms import CreateGradeForm
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
        grades_data = {}
        # grades_data['all_dates'] = []
        # print(queryset)
        for i in queryset:
            if i.subject not in grades_data:
                grades_data[i.subject] = {str(i.grade_date): str(i.value)}
                # if str(i.grade_date) not in grades_data['all_dates']:
                #     grades_data['all_dates'].append(str(i.grade_date))
            else:
                grades_data[i.subject][str(i.grade_date)] = str(i.value)
                # if str(i.grade_date) not in grades_data['all_dates']:
                #     grades_data['all_dates'].append(str(i.grade_date))

        print(grades_data)
        return grades_data


class CreateGradeView(LoginRequiredMixin, CreateView):
    template_name = "teacher_grade_table.html"
    form_class = CreateGradeForm
    success_url = reverse_lazy('teacher_grade_table')


class TeacherTimeTableView(ListView):
    model = TimeTable
    template_name = 'teacher_time_table.html'
    context_object_name = 'time_tables'

    def get_queryset(self):
        queryset = TimeTable.objects.filter(teacher=self.request.user.id).order_by('lesson')
        return queryset
