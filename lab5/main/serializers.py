from rest_framework import serializers
from main.models import TodoList, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("__all__", )


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "name, dateOfCreation, ownerName"


class TodoListSerializerWithTasks(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = TodoList
        fields = "__all__"

