from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


def search_projects(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        projects = Project.objects.filter(owner=request.user, name__contains=searched)
        context = {"searched": searched, "projects": projects}
        return render(request, 'projects/search_projects.html', context)

    else:
        return render(request, 'projects/search_projects.html')
