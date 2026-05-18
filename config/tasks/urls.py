from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path('project/<int:project_id>/create-task/', views.task_create, name='create'),
    path('<int:task_id>/detail/', views.task_detail, name='detail'),
    path('<int:task_id>/update/', views.task_update, name='update'),
    path("<int:task_id>/delete/", views.task_delete, name='delete'),
]
