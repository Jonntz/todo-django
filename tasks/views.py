from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/add-task.html', {'form':form})

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