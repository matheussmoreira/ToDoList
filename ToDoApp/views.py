from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from .models import *
from .forms import *

# AUTHENTICATION

def index(request):
    context = {'user': request.user,}
    return render(request, "auth/base_auth.html", context)

def auth_register(request):  
    if request.method == 'POST':  
        form = RegisterForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('login')
        else:
            # messages.error(request,'Registro inválido!')
            return redirect('register')
    context = {'form': RegisterForm()}  
    return render(request, 'auth/register.html', context)  

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                # messages.success(request, f'Login feito com {user.username}!')
                return redirect('todo_list')
        return redirect('login')
    else:
        context = {'form': LoginForm()}
        return render(request, 'auth/login.html', context)
    
def authenticate(username=None, password=None):
    try:
        user = CustomUser.objects.get(username=username)
        if check_password(password, user.password):
            return user
        return None
    except CustomUser.DoesNotExist:
        return None
    
def auth_logout(request):
    logout(request)
    # messages.success(request, "Deslogado!")
    return redirect('login')

# CRUD

def todo_list(request):
    todos = request.user.todos.all()  
    context = {'todos': todos, 'form': ToDoForm()}
    return render(request, 'todo/todo_list.html', context)


def todo_add(request):
    name = request.POST['name']
    todo = ToDo.objects.create(name=name, user=request.user) 
    return redirect('todo_list')


def todo_update(request, todo_id):
    todo = get_todo(request, todo_id)
    is_checked = request.POST.get('is_checked', False)
    todo.is_checked = (is_checked == 'on')
    todo.save()
    return redirect('todo_list')

def todo_delete(request, todo_id):
    todo = get_todo(request, todo_id)
    todo.delete()  
    return redirect('todo_list')

def get_todo(request, todo_id):
    return ToDo.objects.get(id=todo_id, user=request.user) 
