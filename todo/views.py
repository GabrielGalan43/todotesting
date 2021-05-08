from django.shortcuts import render, redirect
from todo.models import TaskList
from todo.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'todo/index.html')


"""
Esta función incluye al mismo tiempo los métodos,
"Create" y "Read"; de "CRUD".
"""

@login_required
def tasks(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user # owner es el campo definido como ForeignKey.
            instance.save()
            messages.success(request, 'New Task added.')
        return redirect('tasks')
    else:
        # all_tasks = TaskList.objects.all()
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5, orphans=1) # Orphans. Ver referencia en Paginator.Django.
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todo/tasks.html', {'all_tasks': all_tasks})


"""
Esta función realiza el método "Delete" de CRUD.
"""
@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, 'Access Restricted.')
    return redirect('tasks')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task )
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited')
        return redirect('tasks')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'todo/edit.html', {'task_obj': task_obj })    

@login_required
def pending(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'Access Restricted.')
    return redirect('tasks')

@login_required
def completed(request, task_id):    
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'Access Restricted.')
    return redirect('tasks')
