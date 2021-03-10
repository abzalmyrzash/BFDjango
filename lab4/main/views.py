from django.shortcuts import render
from datetime import datetime
from .models import TodoList

# Create your views here.
def uncompleted_list_show(request, list_id):
    toDo = TodoList.objects.get(pk=list_id)
    return render(request, "todo_list.html", {
        "name": toDo.name,
        "tasks": toDo.tasks.filter(mark=False)
    })


def completed_list_show(request, list_id):
    toDo = TodoList.objects.get(pk=list_id)
    return render(request, "completed_todo_list.html", {
        "name": toDo.name,
        "tasks": toDo.tasks.filter(mark=True)
    })
