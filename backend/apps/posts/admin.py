from django.contrib import admin

# Register your models here.
from backend.apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
        'image',
        'author',
        'group',
        'created',
        'updated'
    ]
