from django.db import models
from django.conf import settings
from django.utils import timezone

# Managers
class VisibilityManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(visibility=Task.Visibility.PUBLIC)
        )

# Models
class Task(models.Model):
    class Visibility(models.TextChoices):
        PUBLIC = 'P','Public'
        PRIVATE = 'R', 'Private'

    class Priority(models.IntegerChoices):
        URGENT = 1, 'Urgent'
        HIGH = 2, 'High'
        MEDIUM = 3, 'Medium'
        LOW = 4, 'Low'

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    details = models.TextField()
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    publish_date = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(choices=Priority, default=Priority.LOW)
    visibility = models.CharField(max_length=1, choices=Visibility, default=Visibility.PRIVATE)
    objects = models.Manager()
    visible = VisibilityManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']
        indexes = [
            models.Index(fields=['publish_date',]),
        ]

    def __str__(self):
        return self.title