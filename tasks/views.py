from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and title.strip():
            Task.objects.create(title=title.strip(), description=description.strip() if description else '')
        return redirect('task_list')
    return render(request, 'tasks/task_list.html')
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Ensure title is not None and not empty
        if title is not None and title.strip():
            task.title = title.strip()
            task.description = description.strip() if description else ''
            task.completed = 'completed' in request.POST
            task.save()
            return redirect('task_list')
        else:
            error_message = "Title cannot be empty."
            return render(request, 'tasks/update_task.html', {'task': task, 'error_message': error_message})
    return render(request, 'tasks/update_task.html', {'task': task})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')