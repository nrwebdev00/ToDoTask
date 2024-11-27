from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from faker import Faker
import random
from Task.models import Task

User = get_user_model()

x = random.randint(25, 256)

class Command(BaseCommand):
    help = 'Generate 50 sample tasks'

    def handle(self, *args, **kwargs):
        fake = Faker()
        user = User.objects.get(id=6)

        if not user:
            self.stdout.write(self.style.ERROR('No user found. Please create a user first.'))
            return

        for _ in range(x):
            task = Task.objects.create(
                title=fake.sentence(nb_words=15),
                slug=fake.slug(),
                details=fake.paragraph(nb_sentences=15),
                completed=fake.boolean(chance_of_getting_true=50),
                author=user,
                publish_date=timezone.now(),
                priority=fake.random_element(
                    elements=[Task.Priority.URGENT, Task.Priority.HIGH, Task.Priority.MEDIUM, Task.Priority.LOW]),
                visibility=fake.random_element(elements=[Task.Visibility.PUBLIC, Task.Visibility.PRIVATE]),
                created=timezone.now(),
                updated=timezone.now()
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created task: {task.title}'))

        self.stdout.write(self.style.SUCCESS("Succefully made " + str(x) + " tasks."))
