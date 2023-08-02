from django.forms import ModelForm
from tasks.models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]


class TaskNotesForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "notes",
        ]
