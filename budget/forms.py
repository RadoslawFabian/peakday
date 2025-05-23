from django import forms
from .models import Budget, Expense

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['monthly_income']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']

class IncomeForm(forms.Form):
    amount = forms.DecimalField(label='Add Income', max_digits=10, decimal_places=2)

