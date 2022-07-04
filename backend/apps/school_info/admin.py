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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price'
    ]
    ordering = ['-created']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image',
        'created'
    ]
    ordering = ['-created']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created'
    ]
    ordering = ['-created']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'awesome_class',
        'link'
    ]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'sender_name',
        'title',
        'text'
    ]
