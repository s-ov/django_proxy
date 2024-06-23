from typing import Iterable
from django.db import models


class TaskStatus(models.IntegerChoices):
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)

    def __str__(self) -> str:
        return self.name
    

class InProgressTask(Task):
    class Meta:
        proxy = True

    class  Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.IN_PROGRESS)
        
    def save(self, *args, **kwargs) -> None:
        "When it is added new task make status for it IN_PROGRESS"
        if self._state.adding:
            self.status = TaskStatus.IN_PROGRESS
        super().save(*args, **kwargs)
        
    objects = Manager()


class TodoTask(Task):
    class Meta:
        proxy = True
        ordering = ('created_at',)

    class  Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.TODO)
        
    objects = Manager()


class CompletedTask(Task):
    class Meta:
        proxy = True

    class  Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.COMPLETED)
        
    objects = Manager()

    def __str__(self) -> str:
        return f"Congrats! You've completed '{self.name}' task"
