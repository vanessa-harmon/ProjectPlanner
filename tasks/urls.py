from django.urls import path
from tasks.views import create_task, list_tasks, add_notes_to_task, show_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("<int:id>/", show_task, name="show_task"),
    path("add-notes/<int:id>/", add_notes_to_task, name="add_notes_to_task"),
]
