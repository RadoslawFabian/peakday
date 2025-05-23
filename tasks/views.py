from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Case, When, Value, IntegerField

def task_list(request):
    # Pobranie wyboru sortowania od użytkownika (domyślnie: priority)
    sort_option = request.GET.get('sort', 'priority')

    priority_ordering = Case(
        When(priority='high', then=Value(1)),
        When(priority='medium', then=Value(2)),
        When(priority='low', then=Value(3)),
        output_field=IntegerField(),
    )

    # Wybór sposobu sortowania
    if sort_option == 'priority':
        tasks = Task.objects.all().order_by(priority_ordering, 'deadline')
    else:
        tasks = Task.objects.all().order_by('deadline')

    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form, 'sort_option': sort_option})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form": form, "task": task})
