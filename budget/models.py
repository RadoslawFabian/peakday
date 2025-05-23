from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def remaining_budget(self):
        total_expenses = sum(expense.amount for expense in self.expenses.all())
        return self.monthly_income - total_expenses

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
