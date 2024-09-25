from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
]
