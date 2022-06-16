from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('student/time_table/<int:pk>/', StudentTimeTableView.as_view(), name='student_time_table'),
    path('student/grade_table/<int:pk>', StudentGradeTableView.as_view(), name='student_grade_table')

]
