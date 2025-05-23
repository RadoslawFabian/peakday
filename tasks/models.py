from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = [
    ('high', '🔴 High'),
    ('medium', '🟡 Medium'),
    ('low', '🟢 Low'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.TimeField(null=True, blank=True)  # Zmienione na TimeField

    def __str__(self):
        return self.title
