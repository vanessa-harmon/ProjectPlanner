from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, TaskNotesForm
from tasks.models import Task


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def list_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"tasks": tasks}
    return render(request, "tasks/list.html", context)


def add_notes_to_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskNotesForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task', id=id)
    else:
        form = TaskNotesForm(instance=task)

    context = {
        "form": form,
        "task": task,
    }
    return render(request, 'tasks/add_notes.html', context)


@login_required
def show_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task": task,
    }
    return render(request, "tasks/detail.html", context)
