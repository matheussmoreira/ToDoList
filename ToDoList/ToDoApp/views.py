from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from .forms import *

# AUTHENTICATION PAGES

def index(request):
    return render(request, "seguranca/home_sec.html")

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
            # Should redirect to login instead of duplicating code
            # context = {'form': LoginForm()}
            # return render(request, 'seguranca/login.html', context)
    else:
        context = {'form': UserCreationForm()}
        return render(request,'seguranca/registro.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    context = {'form': LoginForm()}
    return render(request, 'seguranca/login.html', context)

# TODOLIST PAGES

def todo_list(request):
    todos = ToDo.objects.all()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = ToDoForm()
        return render(request, 'todo.html', {'todos': todos, 'form': form})

def delete_todo(request):
    todo_id = request.POST.get('id')
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.is_checked = not todo.is_checked 
        todo.save()
    return redirect('index')