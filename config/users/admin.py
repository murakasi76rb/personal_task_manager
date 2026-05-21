from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from projects.models import Project

class ProjectInline(admin.TabularInline):
    model = Project
    fields = ['title', 'description']
    extra = 1

# @admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = [
        'email', 
        'username', 
        'first_name', 
        'last_name', 
        'is_staff', 
        'phone', 
        'date_joined'
    ]
    list_filter = ['is_staff', 'date_joined']
    search_fields = ['email', 'username', 'first_name', 'last_name']

    inlines = [ProjectInline]
