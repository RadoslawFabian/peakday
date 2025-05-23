from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Budget, Expense
from .forms import BudgetForm, ExpenseForm

@login_required
def budget_view(request):
    budget, created = Budget.objects.get_or_create(user=request.user)
    expenses = budget.expenses.all()
    remaining = budget.remaining_budget()

    if request.method == 'POST':
        if 'save_budget' in request.POST:
            budget_form = BudgetForm(request.POST, instance=budget)
            if budget_form.is_valid():
                budget_form.save()
                return redirect('budget')

        elif 'add_expense' in request.POST:
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense = expense_form.save(commit=False)
                expense.budget = budget
                expense.save()
                return redirect('budget')

    budget_form = BudgetForm(instance=budget)
    expense_form = ExpenseForm()

    context = {
        'budget': budget,
        'expenses': expenses,
        'remaining': remaining,
        'budget_form': budget_form,
        'expense_form': expense_form,
    }
    return render(request, 'budget/budget.html', context)

@login_required
def add_expense(request):
    budget = Budget.objects.get(user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.save()
            return redirect('budget')
    else:
        form = ExpenseForm()
    return render(request, 'budget/add_expense.html', {'form': form})

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, budget__user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('budget')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'budget/edit_expense.html', {'form': form, 'expense': expense})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, budget__user=request.user)
    expense.delete()
    return redirect('budget')
