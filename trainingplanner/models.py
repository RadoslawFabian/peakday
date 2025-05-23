from django.db import models
from django.contrib.auth.models import User

class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    training = models.ForeignKey(Training, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.sets}x{self.reps})"
