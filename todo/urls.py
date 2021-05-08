
from django.urls import path, include
from todo import views

urlpatterns = [     
    path('', views.tasks, name='tasks'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('pending/<task_id>', views.pending, name='pending'),
    path('completed/<task_id>', views.completed, name='completed'),
]
