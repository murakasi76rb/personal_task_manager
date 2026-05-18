from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path('<int:task_id>/detail/', views.task_detail, name='detail'),
    path('<int:task_id>/update/', views.task_update, name='update'),
]
