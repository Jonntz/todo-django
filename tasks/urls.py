from .views import *
from django.urls import path

urlpatterns = [
    path('helloWorld', hello_world),
    path('', task_list, name='task_list'),
    path('yourname/<str:name>', your_name, name="your_name"),
    path('task/<int:id>', task_view, name='task_view'),
]