# TODO 1: import get_object_or_404, redirect, render from django.shortcuts, and require_POST from django.views.decorators.http
from django.shortcuts import get_object_or_404 , redirect, render
from django.views.decorators.http import require_POST
# TODO 2: import TodoForm from .forms and Todo from .models
from .forms import TodoForm
from .models import Todo

# GET /: every todo, newest first (Meta.ordering in models.py sorts them)
def todo_list(request):
    todos = Todo.objects.all()
        return render(request, 'todos/todo_list.html', {'todos': todos})
    return (request, 
    pass
