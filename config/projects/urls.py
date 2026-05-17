from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='list'),
    path('create/', views.project_create, name='create'),
    path('<int:project_id>/detail/', views.project_detail, name='detail'),
]
