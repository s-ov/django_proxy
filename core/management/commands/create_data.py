from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import TaskStatus, Task

# ./manage.py create_data


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        tasks = [
            {'name': 'Learn Python', 'status': 3},
            {'name': 'Learn FastAPI', 'status': 1},
            {'name': 'Learn Django', 'status': 2},
            {'name': 'Learn AJAX', 'status': 1},

        ]

        Task.objects.all().delete()
        for task in tasks:
            Task.objects.create(**task)

        tasks = Task.objects.all()

