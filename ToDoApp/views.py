from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import ToDo
from .forms import *

# AUTHENTICATION

def index(request):
    context = {'user': request.user,}
    return render(request, "auth/base_auth.html", context)

def register(request):  
    if request.method == 'POST':  
        form = RegisterForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('login')
            # context = {'form': LoginForm()}
            # return render(request, 'auth/login.html', context)
        else:
            messages.error(request,'Registro inválido!')
            return redirect('register')
    context = {'form': RegisterForm()}  
    return render(request, 'auth/register.html', context)  

def register2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            # Should redirect to login instead of duplicating code
            context = {'form': LoginForm()}
            return render(request, 'auth/login.html', context)
        else:
            return render(request, "auth/base_auth.html")
    else:
        context = {'form': UserCreationForm()}
        return render(request,'auth/register.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        context = {'form': LoginForm()}
        return render(request, 'auth/login.html', context)

# CRUD

def todo_list(request):
    todos = request.user.todos
    context =  {'todos': todos, 'form': ToDoForm()}
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    name = request.POST['name']
    todo = ToDo.objects.create(name=name)
    request.user.todos.append(todo)
    return redirect('todo_list')

def todo_update(request, todo_id):
    todo = get_todo(request, todo_id)
    is_checked = request.POST.get('is_checked', False)
    if is_checked == 'on':
        is_checked = True
    todo.is_checked = is_checked
    todo.save()
    map(lambda item: todo if item.id == todo_id else item, request.user.todos)
    return redirect('todo_list')

def todo_delete(request, todo_id):
    todo = get_todo(request, todo_id)
    request.user.todos.remove(todo)
    return redirect('todo_list')

# HELPER METHODS

def get_todo(request, todo_id):
    todo_filter = filter(lambda item: item.id == todo_id, request.user.todos)
    return list(todo_filter)[0]