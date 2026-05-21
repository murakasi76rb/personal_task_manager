from django.contrib import admin
from projects.models import Project
from tasks.models import Task

class TaskInline(admin.TabularInline):
    model = Task
    fields = ['title', 'description', 'due_date']
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    list_filter = ['created_at', 'owner']
    search_fields = ['owner__username', 'title']
    list_select_related = ['owner']

    inlines = [TaskInline]
