from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

@login_required
def task_list(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    else:
        task_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(task_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.user = request.user
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/add-task.html', {'form':form})

@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            task.save()
            return redirect('/')
        
        else:
            return render(request, 'tasks/edit-task.html', { 'form': form, 'task': task })

    else:
        return render(request, 'tasks/edit-task.html', { 'form': form, 'task': task })

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso')

    return redirect('/')

@login_required
def change_status(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.done == 'Doing':
        task.done = 'done'
    
    else:
        task.done = 'Doing'
    
    task.save()
    return redirect('/')