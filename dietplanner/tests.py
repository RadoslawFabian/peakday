from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_planner, name="diet_planner"),  # Główna strona dietetyczna
]
