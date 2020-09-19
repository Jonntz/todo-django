from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world")

def task_list(request):
    return render(request, 'tasks/list.html')

def your_name(request, name):
    return render(request, 'tasks/your-name.html', {'name': name})