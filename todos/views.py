from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


# GET /: every todo, newest first (Meta.ordering in models.py sorts them)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos' : todos})


# GET /add/ shows an empty form; POST /add/ saves it
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            return redirect('todo_list')
             todo.save()
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})
    


# POST /toggle/<pk>/: tick a todo off, or undo it. It changes data, so POST only.
@require_POST
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')


@require_POST
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
