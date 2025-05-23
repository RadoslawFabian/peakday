from django.urls import path
from .views import budget_view, add_expense, delete_expense, edit_expense

urlpatterns = [
    path('', budget_view, name='budget'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
]
