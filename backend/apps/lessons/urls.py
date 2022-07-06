from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('student/time_table/<int:pk>/', StudentTimeTableView.as_view(), name='student_time_table'),
    path('student/grade_table/<int:pk>', StudentGradeTableView.as_view(), name='student_grade_table'),
    path('teacher/grade_table/', CreateGradeView.as_view(), name='teacher_grade_table'),
    path('teacher/time_table/<int:pk>/', TeacherTimeTableView.as_view(), name='teacher_time_table'),

]
