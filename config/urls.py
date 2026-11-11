"""
URL configuration for config project.

The urlpatterns list routes URLs to views.
"""
from django.contrib import admin
# TODO 1: import include from django.urls as well, on the line below
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('' , todos/urls.py)
]
