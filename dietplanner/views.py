from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MealPlan
from .forms import MealPlanForm
from datetime import datetime, timedelta

@login_required
def diet_planner(request):
    meal_types = ["Breakfast", "Lunch", "Dinner", "Snack"]
    days = int(request.GET.get("days", 7))
    meals_per_day = int(request.GET.get("meals_per_day", 3))

    if request.method == "POST":
        for j in range(meals_per_day):
            meal_type = request.POST.get(f"meal_type_{j}")
            for i in range(days):
                meal_name = request.POST.get(f"meal_name_{i}_{j}")
                calories = request.POST.get(f"calories_{i}_{j}")
                if meal_name and calories:
                    date = datetime.today().date() + timedelta(days=i)
                    MealPlan.objects.create(
                        user=request.user,
                        date=date,
                        meal_type=meal_type,
                        meal_name=meal_name,
                        calories=int(calories),
                    )
        return redirect("diet_planner")

    return render(request, "dietplanner/diet_planner.html", {
        "meal_types": meal_types,
        "days": range(days),
        "meals_per_day": range(meals_per_day),
    })
