from django.urls import path
from .views import task_list, complete_task, delete_task, edit_task

urlpatterns = [
    path('', task_list, name='task_list'),  # Domyślna strona z listą zadań
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
]
