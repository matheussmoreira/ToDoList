from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDo

def index(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ToDoForm()

    todos = ToDo.objects.all()
    return render(request, 'index.html', {'form': form, 'todos': todos})
