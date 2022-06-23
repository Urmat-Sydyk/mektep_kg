from django.contrib import admin
from backend.apps.school_info.models import *
# Register your models here.

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slogan',
        'founded',
        'address',
        'phone',
        'email',
        'link',
        'work_time',
        'logo',
        'background_image',
        'school_image',
    ]
