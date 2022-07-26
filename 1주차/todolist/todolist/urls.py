"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('todoform/', myapp.views.todo_form, name="todo_form"),
    path('delete/<int:pk>', myapp.views.delete_todo, name="delete_todo"),
    path('edit/<int:pk>', myapp.views.edit_todo, name="edit_todo"),
    path('editpost/<int:pk>', myapp.views.edit_post, name="edit_post"),
    path('complete/<int:pk>', myapp.views.complete_todo, name="complete_todo"),

    path('calendar/', myapp.views.calendar, name="calendar"),
    path('calendar/get', myapp.views.calendar_get, name="calendar_get"),
    path('calendar/delete/<int:pk>', myapp.views.calendar_delete, name="calendar_delete"),
    path('calendar/complete/<int:pk>', myapp.views.calendar_complete, name="calendar_complete"),
    path('calendar/edit/<int:pk>', myapp.views.calendar_edit),
    path('calendar/edit/post/<int:pk>', myapp.views.calendar_edit_post, name="calendar_edit")
]
