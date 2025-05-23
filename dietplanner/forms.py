from django import forms
from .models import MealPlan

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ["date", "meal_type", "meal_name", "calories"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "meal_type": forms.Select(attrs={"class": "form-select"}),
            "meal_name": forms.TextInput(attrs={"class": "form-control"}),
            "calories": forms.NumberInput(attrs={"class": "form-control"}),
        }
