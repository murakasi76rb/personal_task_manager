from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from projects.models import Project
from projects.forms import ProjectForm


def project_list(request: HttpRequest):
    queryset = (Project.objects.prefetch_related('tasks'))
    projects = queryset.filter(owner=request.user)
    context = {
        'projects': projects
    }
    
    return render(request, 'projects/list.html', context)



def project_create(request:HttpRequest):
    if request.method == 'POST':
        form = ProjectForm(request.POST, owner=request.user)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm(owner=request.user)
    context = {
            'form': form
    }
    return render(request, 'projects/create.html', context)


def project_detail(request:HttpRequest, project_id:int):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    tasks = project.tasks.all() #type: ignore
    context = {
        'project': project,
        'tasks': tasks
    }

    return render(request, 'projects/detail.html', context)


def projects_update(request:HttpRequest, project_id:int):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project, owner=request.user)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm(instance=project, owner=request.user)

    context = {
        'form': form
    }
    return render(request, 'projects/update.html', context)

def project_delete(request:HttpRequest, project_id:int):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')
    context = {
        'project': project
    }
    return render(request, 'projects/delete.html', context)

