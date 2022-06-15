from django.contrib import admin

# Register your models here.
from backend.apps.lessons.models import *


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'teacher'
    ]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(RoomNumber)
class RoomNumberAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(ShiftNumber)
class ShiftNumberAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(LessonTime)
class LessonTimeAdmin(admin.ModelAdmin):
    list_display = [
        'number',
        'shift',
        'start',
        'end'
    ]


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = [
        'subject',
        'student_group',
        'teacher',
        'weeks',
        'room',
        'lesson'
    ]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = [
        'value',
        'student',
        'subject',
        'grade_date',
        'teacher'
    ]

