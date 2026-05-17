from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from tasks.models import Task
from tasks.forms import TaskForm
from projects.models import Project

def task_detail(request:HttpRequest, task_id:int):
    queryset = (Task.objects.select_related(
        'project',
        'project__owner'
    ))
    task = get_object_or_404(queryset, pk=task_id, project__owner=request.user)
    context = {
        'task': task
    }
    return render(request, 'tasks/detail.html', context)

def task_create(request:HttpRequest, project_id:int):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            form.save()
            return redirect('projects:detail', project_id=project_id)
    else:
        form = TaskForm(project=project)
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'tasks/create.html', context)


def task_update(request:HttpRequest, task_id:int):
    task = get_object_or_404(Task, pk=task_id, project__owner=request.user)
    project = task.project
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            return redirect('projects:detail', project_id=project.pk)
    else:
        form = TaskForm(instance=task, project=project)
    context = {
        'form': form,
        'task': task,
        'project': project
    }
    return render(request, 'tasks/update.html', context)

def task_delete(request:HttpRequest, task_id:int):
    task = get_object_or_404(Task, pk=task_id, project__owner=request.user)
    project = task.project
    if request.method == 'POST':
        task.delete()
        return redirect('projects:detail', project_id = project.pk)
    context = {
        'task': task,
        'project': project
    }
    return render(request, 'tasks/delete.html', context)


