from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('todo/todo', views.todo_list, name='todo_list'),
    path('todo/add', views.todo_add, name='todo_add'),
    path('todo/update/<int:todo_id>', views.todo_update, name='todo_update'),
    path('todo/delete/<int:todo_id>', views.todo_delete, name='todo_delete'),
]
