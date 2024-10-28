from django.urls import path
from .views import register, user_login, user_logout, task_list, task_create, task_update, task_delete, task_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', task_list, name='task_list'),  # Set task list as the default
    path('task/create/', task_create, name='task_create'),
    path('task/<int:pk>/update/', task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),    
]


