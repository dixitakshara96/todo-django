from django.urls import path

from . import views

# Mounted at '' in config/urls.py, so '' here is the home page and 'add/' is /add/.
# name= lets templates and redirects ask for a URL by name instead of hard-coding it.
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    # TODO: 'add/'              → views.todo_create, named todo_create
    path('add/' , views.todo_create, name = 'todo_create'),
    
    path('toggle/<int:pk>/', views.todo_toggle, name = 'todo_toggle'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    
]
