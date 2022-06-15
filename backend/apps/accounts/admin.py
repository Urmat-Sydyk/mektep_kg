from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'pin',
        'first_name',
        'middle_name',
        'last_name',
        'phone',
        'address',
        'is_active',
        'role'
    ]
    list_editable = ['is_active']


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'parent_phone',
        'student_group'
        ]


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'position',
        'subject'
        ]
