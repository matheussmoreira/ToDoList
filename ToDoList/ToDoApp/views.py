from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm

def index(request):
    todos = ToDo.objects.all()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ToDoForm()

    return render(request, 'index.html', {'todos': todos, 'form': form})

def delete_todo(request):
    todo_id = request.POST.get('id')
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.is_checked = not todo.is_checked 
        todo.save()
    return redirect('index')
