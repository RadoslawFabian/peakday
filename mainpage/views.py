from django.shortcuts import render
from budget.models import Budget, Expense
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    budget, created = Budget.objects.get_or_create(user=request.user)
    expenses = budget.expenses.all()
    remaining_budget = budget.remaining_budget()

    context = {
        'budget': budget,
        'expenses': expenses,
        'remaining_budget': remaining_budget,
    }
    return render(request, 'mainpage/home.html', context)
