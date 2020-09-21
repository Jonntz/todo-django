from .views import *
from django.urls import path

urlpatterns = [
    path('', task_list, name='task_list'),
    path('newtask/', new_task, name='new_task'),
    path('task/<int:id>', task_view, name='task_view'),
    path('edit/<int:id>', task_edit, name='task_view')
]