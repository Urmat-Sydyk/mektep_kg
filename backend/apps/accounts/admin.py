from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.


@admin.register(User)
class AllUserAdmin(UserAdmin):
    list_display = [
        'pin',
        'first_name',
        'middle_name',
        'last_name',
        'phone',
        'address',
        'is_active',
        'role',
    ]
    list_editable = ['is_active']

    add_fieldsets = (
        (None, {'fields': ('pin', 'first_name', 'middle_name',  'last_name', 'phone', 'address', 'is_active', 'role', 'password1', 'password2'), }),
    )
    fieldsets = (
        (None, {'fields': ('pin', 'first_name', 'middle_name',  'last_name', 'phone', 'address', 'is_active', 'role', 'password'), }),
    )
    ordering = ['-id']


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
