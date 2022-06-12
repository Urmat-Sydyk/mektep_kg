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
        'is_active'
    ]
    list_editable = ['is_active']
