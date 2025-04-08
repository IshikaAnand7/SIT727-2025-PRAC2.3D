# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.todo_list, name='todo_list'),  # Route to view the task list
# ]

# todo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # Main view for the task list
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
]

