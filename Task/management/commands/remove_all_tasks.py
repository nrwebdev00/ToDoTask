from django.core.management.base import BaseCommand
from Task.models import Task


class Command(BaseCommand):
    help = 'Remove all tasks from the database'

    def handle(self, *args, **kwargs):
        total_tasks = Task.objects.count()
        if total_tasks == 0:
            self.stdout.write(self.style.WARNING('No tasks found to delete.'))
            return

        Task.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted all {total_tasks} tasks.'))
