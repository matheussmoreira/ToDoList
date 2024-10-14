from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib import messages
from .models import ToDo
from .forms import *

# AUTHENTICATION PAGES

def index(request):
    return render(request, "auth/base_auth.html")

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
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        else:
            messages.error(request,'Nâo foi possível salvar o item!')
            return redirect('todo_list')
    else:
        todos = ToDo.objects.order_by('name')
        context =  {'todos': todos, 'form': ToDoForm()}
        return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    name = request.POST['name']
    ToDo.objects.create(name=name)
    return redirect('todo_list')

def todo_update(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    is_checked = request.POST.get('is_checked', False)
    if is_checked == 'on':
        is_checked = True
    todo.is_checked = is_checked
    todo.save()
    return redirect('todo_list')

def todo_delete(request, todo_id):
    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()
    return redirect('todo_list')


# Old
def todo(request):
    todos = ToDo.objects.all()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        context =  {'todos': todos, 'form': ToDoForm()}
        return render(request, 'todo/todo.html', context)
    
def todo_delete2(request):
    todo_id = request.POST.get('id')
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.is_checked = not todo.is_checked 
        todo.save()
    return redirect('index')