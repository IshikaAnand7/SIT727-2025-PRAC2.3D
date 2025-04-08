# from django.shortcuts import render
# from .models import Task  # Updated to import Task model

# def todo_list(request):
#     tasks = Task.objects.all()  # Updated to fetch tasks instead of todos
#     return render(request, 'todo_list.html', {'tasks': tasks})  # Updated context to tasks

# todo/views.py

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# View to display all tasks and handle the creation of a new task
def todo_list(request):
    tasks = Task.objects.all().order_by('-created_at')  # Fetch all tasks and order by creation time
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task
            return redirect('todo_list')  # Redirect to the same page to refresh the list
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo_list.html', context)

# View to delete a task
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()  # Delete the task
    except Task.DoesNotExist:
        pass  # Handle task not found
    return redirect('todo_list')  # Redirect back to the task list
