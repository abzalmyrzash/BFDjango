from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название списка")
    dateOfCreation = models.DateField(verbose_name="Дата cоздания")

    class Meta:
        verbose_name = "Список заданий"
        verbose_name_plural = "Списки заданий"


class Task(models.Model):
    todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="tasks", verbose_name="Задания списка")
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")
    dateOfCreation = models.DateField(verbose_name="Дата создания")
    deadlineDate = models.DateField(verbose_name="Дедлайн")
    ownerName = models.CharField(max_length=255, null=True, blank="True", verbose_name="Создатель")
    mark = models.BooleanField(default=False, verbose_name="Готовность")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
