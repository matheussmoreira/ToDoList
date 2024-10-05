from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('seguranca/',views.registro, name='registro'),
    path('seguranca/', LoginView.as_view(template_name='seguranca/login.html'), name='login'),
    path('todo/', views.todo_list, name='todo_list'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
]
