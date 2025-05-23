from django.db import models
from django.contrib.auth.models import User

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(
        max_length=20,
        choices=[
            ("Breakfast", "Breakfast"),
            ("Lunch", "Lunch"),
            ("Dinner", "Dinner"),
            ("Snack", "Snack"),
        ],
        null=False,
        blank=False
    )
    meal_name = models.CharField(max_length=100, blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} ({self.date})"
