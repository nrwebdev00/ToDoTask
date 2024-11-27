from django.shortcuts import render, get_object_or_404

from .models import Task

def list_view(request):
    tasks = Task.visible.all()
    context = {'tasks': tasks, 'name':'Nathon', 'page_title': 'Task List'}

    return render(request, 'task/task_list.html', context)

def detail_view(request, id):
    # TODO when authentication is added check is private only show log in user
    task = get_object_or_404(Task, id=id)
    context = {'task': task, 'title': 'Task Details'}
    return render(request, 'task/task_detail.html', context)