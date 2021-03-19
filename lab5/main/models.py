from django.db import models
from auth_.models import MainUser


# Create your models here.
class TodoListQuerySet(models.QuerySet):
    def get_related(self):
        return self.select_related('tasks', 'owner')

    # def get_uncompleted_tasks(self):
    #     return self.tasks.filter(Mark=False)
    #
    # def get_completed_tasks(self):
    #     return self.tasks.filter(Mark=True)


class TodoList(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название списка")
    dateOfCreation = models.DateField(verbose_name="Дата cоздания")
    owner = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name="todos",
                              verbose_name="Списки заданий пользователя")
    objects = TodoListQuerySet.as_manager()

    class Meta:
        verbose_name = "Список заданий"
        verbose_name_plural = "Списки заданий"


class Task(models.Model):
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="tasks", verbose_name="Задания списка")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    dateOfCreation = models.DateField(verbose_name="Дата создания")
    deadlineDate = models.DateField(verbose_name="Дедлайн")
    mark = models.BooleanField(default=False, verbose_name="Готовность")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
