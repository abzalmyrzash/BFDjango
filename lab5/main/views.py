from django.shortcuts import render
from datetime import datetime
from .models import TodoList, Task
from .serializers import TodoListSerializer, TodoListSerializerWithTasks, TaskSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class TodoListViewSet(viewsets.ViewSet, mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin, mixins. ListModelMixin):
    queryset = TodoList.objects.get_related()

    def get_serializer_class(self):
        if self.action in ['list', 'update', 'create']:
            return TodoListSerializer
        if self.action == 'retrieve':
            return TodoListSerializerWithTasks

    def get_permissions(self):  #
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    @action(methods=['GET'], detail=True)
    def completed_list(self, request, **kwargs):
        target_id = int(kwargs['todo_list_id'])
        todo = TodoList.objects.get(pk=target_id)
        queryset = todo.tasks.filter(mark=True)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def uncompleted_list(self, request, **kwargs):
        target_id = int(kwargs['todo_list_id'])
        todo = TodoList.objects.get(pk=target_id)
        queryset = todo.tasks.filter(mark=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ViewSet, mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()


# def uncompleted_list_show(request, list_id):
#     toDo = TodoList.objects.get(pk=list_id)
#     return render(request, "todo_list.html", {
#         "name": toDo.name,
#         "tasks": toDo.tasks.filter(mark=False)
#     })
#
#
# def completed_list_show(request, list_id):
#     toDo = TodoList.objects.get(pk=list_id)
#     return render(request, "completed_todo_list.html", {
#         "name": toDo.name,
#         "tasks": toDo.tasks.filter(mark=True)
#     })
