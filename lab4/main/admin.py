from django.contrib import admin
from .models import Task, TodoList
# # Register your models here.
#


class TodoListAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateOfCreation']
    search_fields = ['name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateOfCreation', 'deadlineDate', 'mark']
    ordering = ['dateOfCreation']
    search_fields = ['name']
    list_filter = ['dateOfCreation', 'deadlineDate', 'mark', 'ownerName']


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Task, TaskAdmin)