from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 
                    'project', 
                    'is_completed', 
                    'due_date', 
                    'created_at', 
                    'updated_at'
    ]
    list_filter = ['is_completed','due_date', 'created_at']
    search_fields = ['project__title', 'title',]
    list_select_related = ['project']
