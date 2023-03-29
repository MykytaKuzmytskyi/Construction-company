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
    TaskCreateView,
    TaskUpdateView,
    EmployeeDeleteView,
    ProjectCreateView,
    closing_task,
    TaskDeleteView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<int:pk>/",
         EmployeeDetailView.as_view(),
         name="employee-detail"
         ),
    path("employees/create/",
         EmployeeCreationView.as_view(),
         name="employee-create"
         ),
    path("employees/update/<int:pk>/",
         EmployeeUpdateView.as_view(),
         name="employee-update"
         ),
    path("employees/delete/<int:pk>/",
         EmployeeDeleteView.as_view(), name="employee-delete"
         ),

    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>",
         ProjectDetailView.as_view(),
         name="project-detail"
         ),
    path("projects/create/",
         ProjectCreateView.as_view(),
         name="project-create"
         ),
    path("projects/update/<int:pk>/",
         ProjectUpdateView.as_view(),
         name="project-update"
         ),
    path("projects/delete/<int:pk>/",
         ProjectDeleteView.as_view(),
         name="project-delete"
         ),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/",
         TaskUpdateView.as_view(),
         name="task-update"
         ),
    path("tasks/delete/<int:pk>/",
         TaskDeleteView.as_view(),
         name="task-delete"
         ),
    path(
        "tasks/<int:pk>/closing-task/",
        closing_task,
        name="closing-tasks",
    ),
]

app_name = "task_manager"
