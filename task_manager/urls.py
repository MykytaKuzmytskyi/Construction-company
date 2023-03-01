from django.urls import path

from task_manager.views import (
    index,
    ProjectListView,
    TaskListView,
    EmployeeListView,
    EmployeeDetailView,
    TaskDetailView,
    ProjectDetailView,
    EmployeeCreationView,
    EmployeeUpdateView,
    TaskCreationView,
)

urlpatterns = [
    path("", index, name="index"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("employees/create/", EmployeeCreationView.as_view(), name="employee-create"),
    path("employees/update/<int:pk>/", EmployeeUpdateView.as_view(), name="employee-update"),

    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>", ProjectDetailView.as_view(), name="project-detail"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create", TaskCreationView.as_view(), name="task-create"),
]

app_name = "task_manager"