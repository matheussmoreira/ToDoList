from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register', views.register, name='register'),
    path('auth/login', views.login, name='login'),
    path('todo/todo', views.todo_list, name='todo_list'),
    path('todo/delete', views.todo_delete, name='todo_delete'),
]
